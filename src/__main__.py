#!/usr/bin/env python3
import sys
import yandereDL
#from colour import terminal_effects

def init(): # logo
    #colour = terminal_effects()
    print("""
                                             _________   _____      _________            _____       /
    //    //    /\            /   ____      /           /     \    /                    /     \     /
     // //     /  \      /\  /   /    \    /-----      /       |  /-----       ====    /      |    /
      /       /    \    /  \/   /      |  /           /_______/  /                    /      /    /
     /       /      \  /       /      /  /_________  /     \    /_________           /      /    /________
                                                    /       \\

    """)
    # coloured
    #print("""
    #{}  _______________________________________________________________________________________________________     {}
    #{}/{}                                          _________   _____      _________{}            _____       /    \ {}
    #{}|{} //    //    /\            /   ____      /           /     \    /         {}           /     \     /      |{}
    #{}|{}  // //     /  \      /\  /   /    \    /-----      /       |  /-----     {}  {}===={}    /      |    /       |{}
    #{}|{}   /       /    \    /  \/   /      |  /           /_______/  /           {}         /      /    /        |{}
    #{}|{}  /       /      \  /       /      /  /_________  /     \    /_________   {}        /      /    /________ |{}
    #{} \________________________________________________{}/{}_______{}\{}______________________________________________ /  {}
    #""".format(colour.black_bg,colour.normal,
    #            colour.black_bg,colour.brightred,colour.white,colour.normal,
    #            colour.black_bg,colour.brightred,colour.white,colour.normal,
    #            colour.black_bg,colour.brightred,colour.white,colour.brightred_bg,colour.normal+colour.white+colour.black_bg,colour.normal,
    #            colour.black_bg,colour.brightred,colour.white,colour.normal,
    #            colour.black_bg,colour.brightred,colour.white,colour.normal,
    #            colour.black_bg,colour.brightred,colour.white,colour.brightred,colour.white,colour.normal))
    print("""
                                        ...... supported sites ......

                                            - yande.re
                                            - danbooru
                                            - gelbooru
                                            - zerochan
                                            - nhentai


    """)
    #del(colour)

def main():
    while True:
        try:
            proc = yandereDL.yandereDL()
        except KeyboardInterrupt:
            print('\n\nerror: user keyboard interrupt. exiting . . .')
            #sys.exit()
            break
        del(proc)


if __name__=='__main__':
    init() # logo
    main()
    sys.exit()
