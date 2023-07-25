from setuptools import setup, find_packages

setup(
   name='MDX23',
   version='1.0',
   description='audio demixer',
   author='Et al.',
   author_email='none',
   packages=find_packages(),
   install_requires=[
       'numpy',
       'soundfile',
       'scipy',
       'torch>=1.8.1',
       'tqdm',
       'librosa',
       'demucs',
       'onnxruntime-gpu',
       'PyQt5',
       'gradio',
       'matplotlib'
   ],
)
