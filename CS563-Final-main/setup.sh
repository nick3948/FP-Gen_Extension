# Set up container for extension experiments
docker pull ucdavisplse/fpgen-artifact:icse20
docker run -it -d --mount src="$(pwd)/"FPGen"",target=/home/fptesting/FPTesting,type=bind --name=FPGen --cpus=8 --memory=32g ucdavisplse/fpgen-artifact:icse20
docker exec FPGen git clone https://github.com/ucd-plse/FPGen.git FPTesting
docker start -ai FPGen


# 
# git clone https://github.com/hmc-alpaqa/metrinome
# cd metrinome/src
# mingw32-make build
# mingw32-make run
# generate extension metrinome file
# copy to metrinome/src/FPGen
# copy meschasch to metrinome (?)
# python3 main.py from docker env
# convert the given list of synthetic/meschasch(?) tests