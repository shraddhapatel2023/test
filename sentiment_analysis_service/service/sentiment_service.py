from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sentiment_analysis_service.enum.http_enum import HttpStatusCodeEnum
from services.response_services import AppServices

response_service = AppServices()
sia = SentimentIntensityAnalyzer()


class SentimentService:
    @staticmethod
    def analyze_sentiment_service(text_data):
        try:
            text_data = text_data
            # Perform sentiment analysis
            sentiment_scores = sia.polarity_scores(text_data)

            # Get the sentiment and compound score
            sentiment = sentiment_scores['compound']

            # Determine sentiment label based on the compound score
            if sentiment >= 0.05:
                sentiment_label = "Positive"
            elif sentiment <= -0.05:
                sentiment_label = "Negative"
            else:
                sentiment_label = "Neutral"
            if sentiment_label:
                response = response_service.app_response(status_code=HttpStatusCodeEnum.OK,
                                                         success=True,
                                                         message="Sentiment Fetched Successfully !!",
                                                         data=[{
                                                             "sentiment": sentiment_label
                                                         }])
                return response
            response = response_service.app_response(status_code=HttpStatusCodeEnum.NOT_FOUND,
                                                     success=False,
                                                     message="Sentiment Not Found, Please Check your text.. !!",
                                                     data=[])
            return response
        except Exception as e:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                     success=False,
                                                     message="Something Went Wrong!",
                                                     data=[])
            return response
