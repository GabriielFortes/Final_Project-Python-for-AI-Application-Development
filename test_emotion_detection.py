import unittest
from Emotion_Detection.emotion_detection import emotion_detector

class TestEmotionDetecton:

    def test_emotion_detection(self):
        test1 = emotion_detector("I am so happy to this hapen")
        self.assertEqual(test1['emotions'], 'bjoy')


unittest.main()
