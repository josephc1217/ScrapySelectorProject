# -*- coding: utf-8 -*-
import scrapy
import scrapy.cmdline

'''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>
'''

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['scrapy.org']
    start_urls = ['https://docs.scrapy.org/en/latest/_static/selectors-sample1.html']

    def parse(self, response):
        #pass
        '''
        result = response.xpath('//title/text()')
        text1 = response.xpath('//title/text()').get()
        text2 = response.xpath('//title/text()').getall()
        print(">>>josephc debug output xpath result = : %s" %result)
        print(">>>josephc debug output xpath text1 = : %s" %text1)
        print(">>>josephc debug output xpath text2 = : %s" %text2)
        
        cssResult = response.css('title::text')    #[<Selector xpath='//title/text()' data='Example website'>]
        cssText1 = response.css('title::text').get()    #Example website
        cssText1 = response.css('title::text').getall()    #['Example website']
        
        print(">>>josephc debug output css result = : %s" %cssResult)    #[<Selector xpath='descendant-or-self::title/text()' data='Example website'>]
        print(">>>josephc debug output css text1 = : %s" %cssText1)    #['Example website']
        print(">>>josephc debug output css text2 = : %s" %cssText1)    #['Example website']    
        '''
        print('\n\n\n======josephc debug ouput begin:')
        
        imgs = response.css('img').xpath('@src').getall()
        for img in imgs:
            print(img)
            
        firstMatchedImageItem = response.xpath('//div[@id="images"]/a/text()').get()
        print(firstMatchedImageItem)
        
        ifExists = response.xpath('//div[@id="not-exists"]/text()').get() is None
        print(ifExists)
        
        ifExists = response.xpath('//div[@id="not-exists"]/text()').get(default='not-found')
        print(ifExists)
        
        imgs = [img.attrib['src'] for img in response.css('img')]        
        print('test print the list %s '%imgs)
        
        firstImageSrc = response.css('img').attrib['src']
        print('first item matched %s'%firstImageSrc)
        
        href = response.css('base').attrib['href']
        print('attrib usage: %s'%href)
        
        getHref1 = response.xpath('//base/@href').get()
        getHref2 = response.css('base::attr(href)').get()
        getHref3 = response.css('base').attrib['href']
        
        print('Get href value way1, //base/@herf = %s'%getHref1)
        print('Get href value way2  base::attr(href) = %s'%getHref2)
        print('Get href value way3 %s'%getHref3)
        
        getListByXpatch1 = response.xpath('//a[contains(@href,"image")]/@href').getall()
        print(getListByXpatch1)
        getListByCSS1 = response.css('a[href*=image]::attr(href)').getall()
        print(getListByCSS1)
        getListByXpatch2 = response.xpath('//a[contains(@href,"image")]/img/@src').getall()
        print(getListByXpatch2)
        getListByCSS2 = response.css('a[href*=image] img::attr(src)').getall()
        print(getListByCSS2)       
        
        print('======josephc debug ouput end. \n\n\n')
