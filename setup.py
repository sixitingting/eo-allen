from setuptools import setup, find_packages


PACKAGE_NAME = 'aicssegmentation'


"""
Notes:
We get the constants MODULE_VERSION from
See (3) in following link to read about versions from a single source
https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
"""

MODULE_VERSION = ""
exec(open(PACKAGE_NAME + "/version.py").read())


def readme():
    with open('README.md') as f:
        return f.read()


test_deps = ['pytest']
lint_deps = ['flake8']
interactive_dev_deps = [
    'matplotlib>=2.0.0',
    'jupyter',
    'itkwidgets'
]
extras = {
    'test_group': test_deps,
    'lint_group': lint_deps,
    'interactive_dev_group': interactive_dev_deps
}

setup(name=PACKAGE_NAME,
      version=MODULE_VERSION,
      description='Scripts for image features calculation.',
      long_description=readme(),
      author='AICS',
      author_email='jianxuc@alleninstitute.org',
      license='Allen Institute Software License',
      packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
      # entry_points={
      #    "console_scripts": [
      #        "cleanup={}.bin.cleanup_1_collect_str_seg:main".format(PACKAGE_NAME)
      #    ]
      # },
      install_requires=[
          'numpy',
          'scipy',
          'pandas',
          'scikit-image>=0.13.1'
      ],

      # For test setup. This will allow JUnit XML output for Jenkins
      setup_requires=['pytest-runner'],
      tests_require=test_deps,

      extras_require=extras,
      zip_safe=False
      )
