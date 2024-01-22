#!/bin/bash

args=''
for i in "$@"; do
    i="${i//\\/\\\\}"
    args="$args \"${i//\"/\\\"}\""
done

if [ "$args" == "" ]; then args="/bin/bash"; fi

if [ -e /dev/nvidia0 ]; then nv="--nv"; fi

singularity exec $nv \
	    --overlay /scratch/work/hockygroup/ss12902/singularity_test_wsGMM/overlay-15GB-500K.ext3:ro \
	    /scratch/work/public/singularity/cuda11.2.2-cudnn8-devel-ubuntu20.04.sif \
            /bin/bash -c "
source /ext3/env.sh
conda activate
$args
exit
"

