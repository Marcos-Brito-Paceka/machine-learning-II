import pandas as pd


class MovieReviewDataset:
    def __init__(self):
        self.train_data = pd.DataFrame({
            'text': [
                # Positive reviews (target=1)
                'The movie was fantastic and well-directed',
                'I really enjoyed the story and characters',
                'A must-watch, brilliant performance by the cast',
                'The special effects were stunning, a visual treat',
                'Great storyline, kept me hooked throughout',
                'The cinematography was beautiful, highly recommend',
                'Engaging from start to finish, loved the direction',
                'An emotional rollercoaster, brought me to tears',
                'The soundtrack was incredible, perfectly matched the scenes',
                'Excellent movie, exceeded my expectations in every way',
                'A thoroughly enjoyable experience, 10/10',
                'Loved the chemistry between the leads, very heartwarming',
                'The plot twists kept me on the edge of my seat',
                "One of the best thrillers I've seen in years",
                'Brilliant direction, a masterpiece of modern cinema',
                'The visual effects were mind-blowing, truly amazing',
                'Outstanding performances, highly recommend watching',
                'The dialogue was witty and entertaining',
                'An unforgettable journey, I loved every moment',

                # Negative reviews (target=0)
                'Too slow-paced, I almost fell asleep',
                'Predictable plot, nothing surprising happened',
                'The acting was terrible and unconvincing',
                'A waste of time, not worth the ticket price',
                'It had a lot of potential but fell flat',
                'I found the dialogue cheesy and unrealistic',
                "Not my kind of movie, I didn't enjoy it",
                'The actors gave a wooden performance, very disappointing',
                'The action scenes were chaotic and hard to follow',
                'Could not connect with the characters, very disappointing',
                'Poorly written script, nothing made sense',
                'Great cinematography but the story was weak',
                'Way too long, could have been much shorter',
                "I didn't enjoy the pacing, felt way too slow",
                "I didn't like the ending, it felt rushed",
                'The editing was poor, it felt disjointed',
                'So much potential, but the story fell flat',
                "I couldn't care less about the characters",
            ],
            'target': [
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1,

                0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0
            ]
        })

        self.test_data = pd.DataFrame({
            'text': [
                'The film was an absolute masterpiece',
                "I couldn't get into the story, too dull for me",
                "I loved the lead actor's performance",
                'The plot made no sense, too many plot holes',
                "One of the best movies I've seen this year",
                'The pacing was too slow for my liking',
                "It's a movie I would watch again and again",
                'The action scenes were poorly choreographed',
                'A truly forgettable movie, nothing stood out',
                'The characters were well-developed and relatable'
            ],
            'target': [1, 0, 1, 0, 1, 0, 1, 0, 0, 1]
        })

    def get_train_data(self):
        return self.train_data

    def get_test_data(self):
        return self.test_data


if __name__ == "__main__":
    dataset = MovieReviewDataset()
    train_df = dataset.get_train_data()
    test_df = dataset.get_test_data()

    print("Train Data:")
    print(train_df)

    print("\nTest Data:")
    print(test_df)
