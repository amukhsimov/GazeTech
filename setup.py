from setuptools import find_packages, setup


if __name__ == '__main__':
    setup(
        name='gaze_tech',
        version='0.1.0',
        description='GazeTech by Yunhan Wang et. al.',
        long_description='This repo is a fork from https://github.com/yunhanwang1105/GazeTech',
        # long_description_content_type='text/markdown',
        author='Akmal Mukhsimov',
        author_email='aka.mukhsimov@gmail.com',
        keywords='computer vision, object detection, eye tracking',
        url='https://github.com/amukhsimov/GazeTech',
        packages=['eth_xgaze', 'eth_xgaze.models'],
        include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        license='Apache License 2.0',
        # install_requires=parse_requirements('requirements/runtime.txt'),
        # extras_require={
        #     'all': parse_requirements('requirements.txt'),
        #     'tests': parse_requirements('requirements/tests.txt'),
        #     'build': parse_requirements('requirements/build.txt'),
        #     'optional': parse_requirements('requirements/optional.txt'),
        # },
        # ext_modules=[],
        # cmdclass={'build_ext': BuildExtension},
        # zip_safe=False
    )