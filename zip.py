import zipfile
import lzma

with zipfile.ZipFile('1min_CANtraffic.zip', 'w', compression=zipfile.ZIP_LZMA) as new_zip:
    new_zip.write('carY/1min_CANtraffic_canid-data.log', arcname='1min_CANtraffic_canid-data.log')