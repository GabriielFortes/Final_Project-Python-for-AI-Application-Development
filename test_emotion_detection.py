import unittest
from Emotion_Detection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):
        test1 = emotion_detector("I am glad this happened")
        domination_emotion = test1['domination_emotion']
        self.assertEqual(domination_emotion, 'joy')

        test1 = emotion_detector("I am really mad about this")
        domination_emotion = test1['domination_emotion']
        self.assertEqual(domination_emotion, 'anger')

        test1 = emotion_detector("I feel disgusted just hearing about this")
        domination_emotion = test1['domination_emotion']
        self.assertEqual(domination_emotion, 'disgust')

        test1 = emotion_detector("I am so sad about this")
        domination_emotion = test1['domination_emotion']
        self.assertEqual(domination_emotion, 'sadness')

        test1 = emotion_detector("I am really afraid that this will happen")
        domination_emotion = test1['domination_emotion']
        self.assertEqual(domination_emotion, 'fear')


if __name__ == "__main__":
    unittest.main()
