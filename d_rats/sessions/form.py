#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from d_rats.sessions import base, file

class FormTransferSession(file.FileTransferSession):
    type = base.T_FORMXFER
