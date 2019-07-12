from setuptools import setup, find_packages

requirements_list = [
    "numpy>=1.16.2",
    "pandas>=0.24.1",
    "click>=7.0",
    "jupyter>=1.0.0",
    "ipykernel>=5.1.0",
    "tqdm>=4.32.1"
]

setup(
    name='recsys',
    version='1.0',
    description="Recsys Challenge",
    long_description="Code for the Recsys Challenge",
    packages=find_packages(),
    install_requires=requirements_list,
    entry_points={
        'console_scripts': [
            'rec-all-viewed-combined-features=recsys.algorithms.all_viewed_combined_features_algorithm.main_rec_all_viewed_combined_features:main',
            'rec-all-viewed-last-booked=recsys.algorithms.all_viewed_last_booked_algorithm.main_rec_all_viewed_last_booked:main',
            'rec-all-viewed=recsys.algorithms.all_viewed_algorithm.main_rec_all_viewed:main',
            'rec-last-hotel-last-booked=recsys.algorithms.last_hotel_last_booked_algorithm.main_rec_last_hotel_last_booked:main',
            'rec-most-hotel=recsys.algorithms.most_hotel_algorithm.main_rec_most_hotel:main',
            'rec-last-hotel=recsys.algorithms.last_hotel_algorithm.main_rec_last_hotel:main',
            'rec-popular=recsys.algorithms.baseline_algorithm.main_rec_popular:main',
            'rec-price=recsys.algorithms.price_algorithm.main_rec_price:main',
            'rec-order=recsys.algorithms.order_algorithm.main_rec_order:main',
            'verify-submission=recsys.submission.verify_submission.verify_subm:main',
            'score-submission=recsys.submission.score_submission.score_subm:main'
        ],
    },
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)
