#! /bin/bash
#comment: run for 60 seconds, change it as per your use
end=$((SECONDS+60))

while [ $SECONDS -lt $end ]; do
    nvidia-smi --format=csv --query-gpu=power.draw,utilization.gpu,memory.used,memory.free,fan.speed,temperature.gpu >> gpu.log
    #comment: or use below command and comment above using #
    #nvidia-smi dmon -i 0 -s mu -d 1 -o TD >> gpu.log
done
