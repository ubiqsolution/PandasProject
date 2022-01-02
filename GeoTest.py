# 도로명주소 위도 경도 값으로 바꿔주기
import pandas as pd
from geopy.geocoders import Nominatim

# csv 파일 불러오기
csv = pd.read_csv('D:/Python/project/PandasProject/mgc.csv')
print(csv.head())

# 데이터프레임 주소값 추출
address = csv['주소']
print(address.head())

# 주소 데이터 깔끔하게 다듬기
for i in range(len(address)):
    a = address[i].split(' ')
    address[i] = " ".join(a[0:4])
print(address)

geo_local = Nominatim(user_agent='South Korea')

# 위도, 경도 반환하는 함수
def geocoding(address):
    geo = geo_local.geocode(address)
    x_y = [geo.latitude, geo.longitude]
    return x_y

# 주소를 위,경도 값으로 변환하기
latitude = []
longitude = []

if address is not None:
    for i in address:
        latitude.append(geocoding(i)[0])
        longitude.append(geocoding(i)[1])

print(latitude, longitude)