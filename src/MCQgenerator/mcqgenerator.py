import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from mcqgenrator.utils import read_file,get_table_data
from mcqgenrator.logger import logging