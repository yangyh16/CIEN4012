# CIEN4012
Hi everyone, welcome to the labs of Sustainable Urban Systems Engineering (CIEN4012)! With all the disciplinary input from lectures, now it is time to start some practice.

## Requirement

It's up to you how to run the tutorial notebook. If you have no experience in python before, there are some ways to start.

**Google Colab**

[Google Colab](https://colab.google/) is a good option to start. There are some advantages of Google Colab: easy to share, great for collaboration, convenient version control, choice of computational resources, etc. There is a [basic tutorial](https://colab.research.google.com/drive/16pBJQePbqkz3QFV54L4NIkOn1kwpuRrj) on how to start with Google Colab.

**Basics**

If you would like to run the tutorial on your local machine, here is some recommended setup:

- Python (version: no later than 3.9)
- A code/text editor (for example, vscode)

**Python installation**

This tutorial is run in Python. If you would like to run the tutorial locally, please have Python installed. Please go to the offcicial Python website at https://www.python.org/downloads/, and download the corresponding Python installer for your system. Then, run the installer on your laptop and follow the on-screen instructions.

Note that during the installation process, you may be asked to select certain configuration options such as adding Python to your system PATH or installing additional packages. You can choose the default options for most of these prompts, but make sure to read each one carefully to ensure that you are installing Python in the way that you want.

**Virtual environment**

Virtual environment is a great tool to separate packages from projects and thus to avoid a mess. For example, you can use Python's virtual environment `virtualenv` (tutorial: https://docs.python.org/3/tutorial/venv.html) or `conda` (installation: https://conda.io/projects/conda/en/latest/user-guide/install/index.html; start guide: https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).

**Package requirement**

The following packages are required to be downloaded beforehead:

- `numpy`

- `pandas`

- `matplotlib`

- `geopandas`

- `shapely`


## Lab 1
Hudson Yards is a newly built business center in NYC attracting numerous people for diverse activities. In Lab 1, we will aggregate taxi flows to Hudson yards and investigate potential correlated factors. After going through the tutorial, we will get some basic skills in urban analytics - data analysis, spatial mapping, data visualization, etc. Have fun!

![hudson_yards](https://github.com/yangyh16/CIEN4012/assets/160519828/0143ad43-8d18-4ad4-a7e3-50bfa8041c70)

**Notice**
To run this tutorial, all the files in this GitHub page have to be downloaded. Besides, the taxi data is downloaded from [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Please change the corresponding file name if you download a different day or taxi type.

Once all data is downloaded, open and try to run `Lab1.ipynb`.
