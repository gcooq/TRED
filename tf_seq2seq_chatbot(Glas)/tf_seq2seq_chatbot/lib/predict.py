import os

import tensorflow as tf

from tf_seq2seq_chatbot.configs.config import TEST_DATASET_PATH, FLAGS
from tf_seq2seq_chatbot.lib import data_utils
from tf_seq2seq_chatbot.lib.seq2seq_model_utils import create_model, get_predicted_sentence


def predict():
    def _get_test_dataset():
        with open(TEST_DATASET_PATH) as test_fh:
            test_sentences = [s.strip() for s in test_fh.readlines()]
        return test_sentences

    results_filename = '_'.join(['results', str(FLAGS.num_layers), str(FLAGS.size), str(FLAGS.vocab_size)])
    results_path = os.path.join(FLAGS.results_dir, results_filename)

    with tf.Session() as sess, open(results_path, 'w') as results_fh:
        # Create model and load parameters.
        model = create_model(sess, forward_only=True)
        model.batch_size = 1  # We decode one sentence at a time.

        # Load vocabularies.
        vocab_path = os.path.join(FLAGS.data_dir, "vocab%d.in" % FLAGS.vocab_size)
        vocab, rev_vocab = data_utils.initialize_vocabulary(vocab_path)

        test_dataset = _get_test_dataset()

        i = 0
        allright = 0
        for sentence in test_dataset:
            # Get token-ids for the input sentence.
            if i%2 == 0:
                predicted_sentence = get_predicted_sentence(sentence, vocab, rev_vocab, model, sess)
                item = sentence.strip().split(',')
                predicted_sentence = item[0] +','+ predicted_sentence+',' +item[1]
                print(sentence, ' -> ', predicted_sentence)
                # results_fh.write(sentence + ' -> ' + predicted_sentence + '\n')

            if i%2 == 1:
                item = predicted_sentence.strip().split(',')
                sentence = item[0] +','+ sentence+',' +item[-1]
                if sentence == predicted_sentence:
                    allright += 1
                    print('^ is allright'+'\n')
                    # results_fh.write('^ is allright'+'\n')
                    results_fh.write(sentence+'\n'+predicted_sentence+'\n')
                else:
                    # print('Error~right is %s' %sentence)
                    # results_fh.write('Error~right is %s' %sentence+'\n')
                    results_fh.write(sentence+'\n'+predicted_sentence+'\n')
            i = i + 1

            

        print 'traj=',i/2,',allright=',allright,',accuracy=',allright*1.0/(i*1.0/2)
        results_fh.write('traj=%d,allright=%d,accuracy=%f'%(i/2,allright,allright*1.0/(i*1.0/2)))