#!/bin/bash

SIMULATE="simulate"
STATE="$SIMULATE/state"


QSUB=$(command -v qsub)

if [ -n "$QSUB" ]; then
    # save PBS_JOBID in state file via tee
    echo "INFO: Submitting job via pbs schedular"
    qsub -o log.qsub.stdout -e log.qsub.stderr pbs.sh | tee $STATE/pbs_job_id
else
    echo "INFO: Running job in place"
    echo $$ > $STATE/bash_job_pid
    $HOME/miniconda/bin/python entry.py
fi