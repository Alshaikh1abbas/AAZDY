{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 Consolas;}
{\colortbl;\red255\green255\blue255;\red27\green31\blue34;\red255\green255\blue255;\red109\green109\blue109;
}
{\*\expandedcolortbl;;\cssrgb\c14118\c16078\c18039;\cssrgb\c100000\c100000\c100000;\cssrgb\c50196\c50196\c50196;
}
\margl1440\margr1440\vieww43200\viewh25340\viewkind0
\deftab720

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trcbpat3 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth9240\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth9240\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\cell
\pard\intbl\itap1\pardeftab720\sl400\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #!/usr/bin/env python\
import sys\
from twython import Twython\
from picamera import PiCamera\
from time import sleep\
#Ali69777725\
\
apiKey = 'YlAEbs0q2JpxPrEcIBDgDSlTA'\
apiSecret = 'OY8rlFOy5a5D52Ectwj346O8GWnSLxVSY5I5Iak8RTgW6DCyFN'\
accessToken = '2525841722-0XQ8m3WpSyXeCHsxtMKYNgmMkyfNWY2OpGpaPoD'\
accessTokenSecret = 'bHUsD99zlmV7pxqqoPjH3cm9ZqPywWfggUdnPtLZaoVlT'\
twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)\
\
camera = PiCamera()\
camera.start_preview(fullscreen=False,window=(500,200,1024,768))\
sleep(5)\
camera.capture('image.jpg')\
msg = 'Please work'\
with open('image.jpg', 'rb') as photo:\
    twitter.update_status_with_media(status=msg, media = photo)\
exit()\cell \lastrow\row}