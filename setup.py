from setuptools import setup

# build package command: python setup.py bdist_wheel
# release package command: twine upload dist/KoreaNewsCrawler-${version}-py3-none-any.whl

setup(
    name             = 'KoreaNewsCrawler',
    version          = '0.1',
    description      = 'Crawl the korean news',
    author           = 'SangJun Yoon',
    author_email     = 'yoonsj0322@gmail.com',
    url              = 'https://github.com/SangJunni/NewsCrawler',
    install_requires = ['requests', 'beautifulsoup4'],
    packages         = ['news_crawler'],
    keywords         = ['crawl', 'NaverNews', 'crawler'],
    python_requires  = '>=3.6',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3.6'
    ]
)