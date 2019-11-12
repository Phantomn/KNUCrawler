#!/bin/bash

cd /home/phantom/KNUCrawler/knu/knu
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl knu
