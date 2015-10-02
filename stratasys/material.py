# Copyright (c) 2013, Benjamin Vanheuverzwijn <bvanheu@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <BENJAMIN VANHEUVERZWIJN> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#
# A material is a type of plastic used to make 3D prototype
# It might have some information like optimal working temperature, etc.
#

id_to_name = ["unknown"] * 0x200
id_to_name[0x00] = "ABS"
id_to_name[0x01] = "ABS_RED"
id_to_name[0x02] = "ABS_GRN"
id_to_name[0x03] = "ABS_BLK"
id_to_name[0x04] = "ABS_YEL"
id_to_name[0x05] = "ABS_BLU"
id_to_name[0x06] = "ABS_CST"
id_to_name[0x07] = "ABSI"
id_to_name[0x08] = "ABSI_RED"
id_to_name[0x09] = "ABSI_GRN"
id_to_name[0x0a] = "ABSI_BLK"
id_to_name[0x0b] = "ABSI_YEL"
id_to_name[0x0c] = "ABSI_BLU"
id_to_name[0x0d] = "ABSI_AMB"
id_to_name[0x0e] = "ABSI_CST"
id_to_name[0x0f] = "ABS_S"
id_to_name[0x10] = "PC"
id_to_name[0x11] = "PC_RED"
id_to_name[0x12] = "PC_GRN"
id_to_name[0x13] = "PC_BLK"
id_to_name[0x14] = "PC_YEL"
id_to_name[0x15] = "PC_BLU"
id_to_name[0x16] = "PC_CST"
id_to_name[0x17] = "PC_S"
id_to_name[0x18] = "ULT9085"
id_to_name[0x19] = "ULT_RED"
id_to_name[0x1a] = "ULT_GRN"
id_to_name[0x1b] = "ULT_BLK"
id_to_name[0x1c] = "ULT_YEL"
id_to_name[0x1d] = "ULT_BLU"
id_to_name[0x1e] = "ULT_CST"
id_to_name[0x1f] = "ULT_S"
id_to_name[0x20] = "PPSF"
id_to_name[0x21] = "PPSF_RED"
id_to_name[0x22] = "PPSF_GRN"
id_to_name[0x23] = "PPSF_BLK"
id_to_name[0x24] = "PPSF_YEL"
id_to_name[0x25] = "PPSF_BLU"
id_to_name[0x26] = "PPSF_CST"
id_to_name[0x27] = "PPSF_S"
id_to_name[0x28] = "ABS_SS"
id_to_name[0x29] = "P401"
id_to_name[0x2a] = "P401_RED"
id_to_name[0x2b] = "P401_GRN"
id_to_name[0x2c] = "P401_BLK"
id_to_name[0x2d] = "P401_YEL"
id_to_name[0x2e] = "P401_BLU"
id_to_name[0x2f] = "P401_CST"
id_to_name[0x30] = "ABS_SGRY"
id_to_name[0x31] = "ABS_GRY"
id_to_name[0x33] = "ABSI_GRY"
id_to_name[0x3c] = "P430"
id_to_name[0x3d] = "P430_RED"
id_to_name[0x3e] = "P430_GRN"
id_to_name[0x3f] = "P430_BLK"
id_to_name[0x40] = "P430_YEL"
id_to_name[0x41] = "P430_BLU"
id_to_name[0x42] = "P430_CST"
id_to_name[0x43] = "P430_GRY"
id_to_name[0x44] = "P430_NYL"
id_to_name[0x45] = "P430_ORG"
id_to_name[0x46] = "P430_FLS"
id_to_name[0x47] = "P430_IVR"
id_to_name[0x50] = "ABS_M30I"
id_to_name[0x51] = "ABS_ESD7"
id_to_name[0x64] = "PCABSWHT"
id_to_name[0x65] = "PCABSRED"
id_to_name[0x66] = "PCABSGRN"
id_to_name[0x67] = "PC_ABS"
id_to_name[0x68] = "PCABSYEL"
id_to_name[0x69] = "PCABSBLU"
id_to_name[0x6a] = "PCABSCST"
id_to_name[0x6b] = "PCABSGRY"
id_to_name[0x78] = "SR20"
id_to_name[0x82] = "PC_SR"
id_to_name[0x8c] = "ABS_M30"
id_to_name[0x8d] = "M30_RED"
id_to_name[0x8e] = "M30_GRN"
id_to_name[0x8f] = "M30_BLK"
id_to_name[0x90] = "M30_YEL"
id_to_name[0x91] = "M30_BLU"
id_to_name[0x92] = "M30_CST"
id_to_name[0x93] = "M30_GRY"
id_to_name[0x94] = "M30_SGRY"
id_to_name[0x95] = "M30_WHT"
id_to_name[0x96] = "M30_SIL"
id_to_name[0xa0] = "ABS_S_2"
id_to_name[0xaa] = "ABS_SS_2"
id_to_name[0xab] = "SR30"
id_to_name[0xad] = "ULT_S2"
id_to_name[0xae] = "SR_100"
id_to_name[0xb4] = "PC_ISO"
id_to_name[0xbe] = "PC_ISO_T"
id_to_name[0xbf] = "P1_5M1"
id_to_name[0xc0] = "P1_5M2"
id_to_name[0xc1] = "P1_5M3"
id_to_name[0xc6] = "Rddev"
id_to_name[0xc7] = "RddevS"
id_to_name[0xc8] = "RD1"
id_to_name[0xc9] = "RD2"
id_to_name[0xca] = "RD3"
id_to_name[0xcb] = "RD4"
id_to_name[0xcc] = "RD5"
id_to_name[0xcd] = "RD-S1"
id_to_name[0xce] = "RD-S2"
id_to_name[0xcf] = "RD-S3"
id_to_name[0xd0] = "RD-S4"
id_to_name[0xd1] = "RD-S5"
id_to_name[0xfa] = "uP430"
id_to_name[0xfb] = "uP430_RED"
id_to_name[0xfc] = "uP430_GRN"
id_to_name[0xfd] = "uP430_BLK"
id_to_name[0xfe] = "uP430_YEL"
id_to_name[0xff] = "uP430_BLU"
id_to_name[0x100] = "uP430_GRY"
id_to_name[0x118] = "SR30XL"
id_to_name[0x119] = "P430XL_IVR"
id_to_name[0x11a] = "P430XL"
id_to_name[0x11b] = "P430XL_RED"
id_to_name[0x11c] = "P430XL_GRN"
id_to_name[0x11d] = "P430XL_BLK"
id_to_name[0x11e] = "P430XL_YEL"
id_to_name[0x11f] = "P430XL_BLU"


name_to_id = {}

def get_name_from_id(id):
    return id_to_name[id]

def get_id_from_name(name):
    if len(name_to_id) == 0:
        for key, value in enumerate(id_to_name):
            name_to_id[value] = key

    return name_to_id[name]