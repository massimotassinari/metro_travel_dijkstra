"""
EJEMPLOS DE ESTRUCTURAS
"""
visa_costo = {
    "AUA": [("CCS", 40.0), ("CUR", 15.0), ("BON", 15.0), ("SXM", 85.0)],
    "BGI": [("CCS", 180.0), ("POS", 35.0), ("SXM", 70.0)],
    "BON": [("CCS", 60.0), ("AUA", 15.0), ("CUR", 15.0)],
    "CCS": [
        ("AUA", 40.0),
        ("CUR", 35.0),
        ("BON", 60.0),
        ("SDQ", 180.0),
        ("POS", 150.0),
        ("BGI", 180.0),
    ],
    "CUR": [("CCS", 35.0), ("AUA", 15.0), ("BON", 15.0), ("SXM", 80.0)],
    "FDF": [("POS", 75.0)],
    "POS": [("CCS", 150.0), ("BGI", 35.0), ("SXM", 90.0), ("PTP", 80.0), ("FDF", 75.0)],
    "PTP": [("POS", 80.0), ("SXM", 100.0), ("SBH", 80.0)],
    "SBH": [("SXM", 45.0), ("PTP", 80.0)],
    "SDQ": [("CCS", 180.0), ("SXM", 50.0)],
    "SXM": [
        ("SDQ", 50.0),
        ("SBH", 45.0),
        ("POS", 90.0),
        ("BGI", 70.0),
        ("PTP", 100.0),
        ("CUR", 80.0),
        ("AUA", 85.0),
    ],
}

no_visa_costo = {
    "AUA": [("CCS", 40.0), ("CUR", 9999), ("BON", 9999), ("SXM", 9999)],
    "BGI": [("CCS", 180.0), ("POS", 35.0), ("SXM", 9999)],
    "BON": [("CCS", 60.0), ("AUA", 9999), ("CUR", 9999)],
    "CCS": [
        ("AUA", 9999),
        ("CUR", 9999),
        ("BON", 9999),
        ("SDQ", 9999),
        ("POS", 150.0),
        ("BGI", 180.0),
    ],
    "CUR": [("CCS", 35.0), ("AUA", 9999), ("BON", 9999), ("SXM", 9999)],
    "FDF": [("POS", 75.0)],
    "POS": [("CCS", 150.0), ("BGI", 35.0), ("SXM", 9999), ("PTP", 80.0), ("FDF", 75.0)],
    "PTP": [("POS", 80.0), ("SXM", 9999), ("SBH", 80.0)],
    "SBH": [("SXM", 9999), ("PTP", 80.0)],
    "SDQ": [("CCS", 180.0), ("SXM", 9999)],
    "SXM": [
        ("SDQ", 9999),
        ("SBH", 45.0),
        ("POS", 90.0),
        ("BGI", 70.0),
        ("PTP", 100.0),
        ("CUR", 9999),
        ("AUA", 9999),
    ],
}

visa_escalas = {
    "AUA": [("CCS", 1), ("CUR", 1), ("BON", 1), ("SXM", 1)],
    "BGI": [("CCS", 1), ("POS", 1), ("SXM", 1)],
    "BON": [("CCS", 1), ("AUA", 1), ("CUR", 1)],
    "CCS": [("AUA", 1), ("CUR", 1), ("BON", 1), ("SDQ", 1), ("POS", 1), ("BGI", 1)],
    "CUR": [("CCS", 1), ("AUA", 1), ("BON", 1), ("SXM", 1)],
    "FDF": [("POS", 1)],
    "POS": [("CCS", 1), ("BGI", 1), ("SXM", 1), ("PTP", 1), ("FDF", 1)],
    "PTP": [("POS", 1), ("SXM", 1), ("SBH", 1)],
    "SBH": [("SXM", 1), ("PTP", 1)],
    "SDQ": [("CCS", 1), ("SXM", 1)],
    "SXM": [
        ("SDQ", 1),
        ("SBH", 1),
        ("POS", 1),
        ("BGI", 1),
        ("PTP", 1),
        ("CUR", 1),
        ("AUA", 1),
    ],
}

no_visa_escalas = {
    "AUA": [("CCS", 1), ("CUR", 9999), ("BON", 9999), ("SXM", 9999)],
    "BGI": [("CCS", 1), ("POS", 1), ("SXM", 9999)],
    "BON": [("CCS", 1), ("AUA", 9999), ("CUR", 9999)],
    "CCS": [
        ("AUA", 9999),
        ("CUR", 9999),
        ("BON", 9999),
        ("SDQ", 9999),
        ("POS", 1),
        ("BGI", 1),
    ],
    "CUR": [("CCS", 1), ("AUA", 9999), ("BON", 9999), ("SXM", 9999)],
    "FDF": [("POS", 1)],
    "POS": [("CCS", 1), ("BGI", 1), ("SXM", 9999), ("PTP", 1), ("FDF", 1)],
    "PTP": [("POS", 1), ("SXM", 9999), ("SBH", 1)],
    "SBH": [("SXM", 9999), ("PTP", 1)],
    "SDQ": [("CCS", 1), ("SXM", 9999)],
    "SXM": [
        ("SDQ", 9999),
        ("SBH", 1),
        ("POS", 1),
        ("BGI", 1),
        ("PTP", 1),
        ("CUR", 9999),
        ("AUA", 9999),
    ],
}
"""Tabla auxiliar"""

"""Inicial"""
{
    "AUA": [0, "", False],
    "BGI": [999, "", False],
    "BON": [999, "", False],
    "CCS": [999, "", False],
    "CUR": [999, "", False],
    "FDF": [999, "", False],
    "POS": [999, "", False],
    "PTP": [999, "", False],
    "SBH": [999, "", False],
    "SDQ": [999, "", False],
    "SXM": [999, "", False],
}
"""Final"""
{
    "AUA": [40.0, "CCS", True],
    "BGI": [180.0, "CCS", True],
    "BON": [50.0, "CUR", True],
    "CCS": [0, "", True],
    "CUR": [35.0, "CCS", True],
    "FDF": [225.0, "POS", True],
    "POS": [150.0, "CCS", True],
    "PTP": [215.0, "SXM", True],
    "SBH": [160.0, "SXM", True],
    "SDQ": [165.0, "SXM", True],
    "SXM": [115.0, "CUR", True],
}
