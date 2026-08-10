from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="review-removal-intelligence",
    version="1.0.0",
    author="ReviewRemoval.Services",
    author_email="info@reviewremoval.services",
    description="Review Removal Intelligence is an automated review management system designed to streamline the identification, analysis, and tracking of problematic online reviews.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://reviewremoval.services",
    project_urls={
        "Homepage": "https://reviewremoval.services",
        "GitHub": "https://github.com/review-removal-services/review-removal-intelligence",
        "Documentation": "https://review-removal-intelligence.readthedocs.io",
        "PyPI": "https://pypi.org/project/review-removal-intelligence",
    },
    py_modules=["review_intelligence"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "review-removal",
        "review-intelligence",
        "fake-review-detection",
        "online-review-monitoring",
        "policy-compliance",
        "review-analysis",
        "reputation-management",
        "review-management",
    ],
    entry_points={
        "console_scripts": [
            "review-removal-intel=review_intelligence:main",
        ],
    },
)
