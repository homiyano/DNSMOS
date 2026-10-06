"""Runs the unmodified DNS-Challenge/DNSMOS/dnsmos_local.py with a librosa>=0.10 compatibility shim.
Usage: python run_dnsmos.py -t <wav_dir> -o <out.csv> [-p]
"""
import os, runpy, sys
import librosa

_resample = librosa.resample
librosa.resample = lambda y, orig_sr, target_sr, **kw: _resample(y, orig_sr=orig_sr, target_sr=target_sr, **kw)

# Make relative model paths ('DNSMOS/...') resolve; keep user paths absolute.
args = sys.argv[1:]
for flag in ("-t", "-o"):
    if flag in args:
        i = args.index(flag) + 1
        args[i] = os.path.abspath(args[i])
sys.argv = ["dnsmos_local.py"] + args
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "DNS-Challenge", "DNSMOS"))
runpy.run_path("dnsmos_local.py", run_name="__main__")
