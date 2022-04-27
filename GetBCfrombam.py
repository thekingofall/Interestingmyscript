import pysam
import os,sys




def Get_BCfrombam(inputbam,bcfile,outdir):
    samfile = pysam.AlignmentFile(inputbam, "rb")
    namedir=[]
    dataname=open(bcfile,"r+")
    for i in dataname:
        print(i.rstrip("\n"))
        if  i.rstrip("\n") !='':
            namedir.append(i.rstrip("\n"))
    # print(namedir)
    os.system("mkdir -p "+outdir)
    for i in range(0,len(namedir)):

        locals() [namedir[i]]=pysam.AlignmentFile(outdir+"/"+namedir[i]+".bam", "wb", template=samfile)
    for read in samfile.fetch():
        TAG=dict(read.tags)
        CB=TAG["CB"]
        # print(TAG["CB"])
        tem=read
        # print(tem)
        # if i ==10:
        #     break
        # i+=1
        if CB in namedir:
            locals()[CB].write(read)

if __name__ == '__main__':
    infilebam = sys.argv[1]
    barcodefile = sys.argv[2]
    outfile=sys.argv[3]
    Get_BCfrombam(inputbam=infilebam,bcfile=barcodefile,outdir=outfile)

