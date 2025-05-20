rm -r recursive-summation/
cp -r template/ recursive-summation/
cd recursive-summation

for i in $(seq 1 $1); 
do
    for file in $(find ./ -name '*.c')
    do
        sed -i -e 's/REPLACE/REPLACE\n\tfor(int k=0;k<2;k++)/' $file
    done
done

cd ../
