# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:56:04 2019

@author: gdldilop
"""
import fire
import logging

logger = logging.getLogger(__name__)

from util import print_name

class Main(object):
    
    def print_message(self, content) :
        logger.info(content)
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)