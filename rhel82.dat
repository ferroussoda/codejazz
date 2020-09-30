cd /sys/devices/system/cpu/; for i in `seq 40 143`; do echo 0 > cpu$i/online & echo $i; done; cd /root/rhel-kernels/byte-unixbench/UnixBench/pgms

To rh83sp1: kexec ./vmlinuz-4.18.0-232.el8.ppc64le --initrd="./initramfs-4.18.0-232.el8.ppc64le.img"

To rhel82:  kexec ./vmlinuz-4.18.0-193.el8.ppc64le --initrd="./initramfs-4.18.0-193.el8.ppc64le.img"

[root@zz8c-p2 pgms]# perf record -e instructions -g numactl -C 1 ./context1 1
COUNT|173612|1|lps
COUNT|173612|1|lps
[ perf record: Woken up 3 times to write data ]
[ perf record: Captured and wrote 0.627 MB perf.data (4009 samples) ]
[root@zz8c-p2 pgms]# perf stat -r 5 ./context1 1
COUNT|119636|1|lps
COUNT|119637|1|lps
COUNT|109060|1|lps
COUNT|109061|1|lps
COUNT|120341|1|lps
COUNT|120342|1|lps
COUNT|120982|1|lps
COUNT|120983|1|lps
COUNT|117751|1|lps
COUNT|117752|1|lps

 Performance counter stats for './context1 1' (5 runs):

            933.52 msec task-clock                #    0.933 CPUs utilized            ( +-  0.15% )
           235,103      context-switches          #    0.252 M/sec                    ( +-  1.86% )
                 6      cpu-migrations            #    0.006 K/sec                    ( +- 25.63% )
                57      page-faults               #    0.061 K/sec                    ( +-  1.20% )
     2,441,412,715      cycles                    #    2.615 GHz                      ( +-  0.14% )  (33.16%)
       163,751,115      stalled-cycles-frontend   #    6.71% frontend cycles idle     ( +-  3.19% )  (50.13%)
     1,254,732,956      stalled-cycles-backend    #   51.39% backend cycles idle      ( +-  0.73% )  (17.21%)
     2,299,276,286      instructions              #    0.94  insn per cycle         
                                                  #    0.55  stalled cycles per insn  ( +-  2.23% )  (32.62%)
       445,419,639      branches                  #  477.142 M/sec                    ( +-  1.96% )  (49.87%)
         4,408,971      branch-misses             #    0.99% of all branches          ( +-  1.31% )  (15.04%)

         1.0008096 +- 0.0000344 seconds time elapsed  ( +-  0.00% )

