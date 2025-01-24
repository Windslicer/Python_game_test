from setuptools import setup, find_packages

setup(
    name='python_game_test',  # Replace with your package name
    version='0.0.1',
    description='A collection of CLI-based games: Stone-Paper-Scissors, Odd or Even, and Word Guessing.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/windslicer',  # Replace with your GitHub repo URL
    author='Atharv Kanawade',
    author_email='Kanawadeatharva29@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'stone-paper-scissors=my_game_package.stone_paper_scissors:play',
            'odd-or-even=my_game_package.odd_or_even:odd_or_even_game',
            'word-guessing=my_game_package.word_guessing_game:word_guessing_game',
        ],
    },
)
