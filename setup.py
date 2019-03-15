from setuptools import setup, find_packages

requirements_list = [
    "numpy>=1.16.2",
    "pandas>=0.24.1",
    "click>=7.0",
    "jupyter>=1.0.0",
    "ipykernel>=5.1.0"
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
            'rec-popular=recsys.algorithms.baseline_algorithm.rec_popular:main',
            'rec-price=recsys.algorithms.price_algorithm.rec_price:main',
            'verify-submission=recsys.submission.verify_submission.verify_subm:main',
            'score-submission=recsys.submission.score_submission.score_subm:main'
        ],
    },
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)
