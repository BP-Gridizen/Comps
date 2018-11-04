# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:14:21 2018

@author: Burhanuddin
************************ INPUT ENTRY *************************************************************** """

post_code = 'se152dy'
"""post_code has to be entered inside quotation marks ' '. If done correctly it'll be same colour as this.
make sure postcode has no spaces ie 'sw73bq'  """

radius = 0.5       #in miles 
minimum_beds = 1
maximum_beds = 4  #these values are inclusive
percentile = 0.8  #comps percentile to use as a decimal
"""these values have no quotation marks. Should be a red brown colour"""

auto_filter_on = 'Y'
save_flag = 'Y'
"""this is either 'Y' or 'N' """
website = "http://api.zoopla.co.uk/api/v1/property_listings.js"

"""************************ ACTUAL CODE ****************************************************************** """
import functions as fn


sales_comps = fn.full_comps_calc(website, post_code, radius, minimum_beds, maximum_beds, "sale", percentile, auto_filter_on, save_flag)
rental_comps = fn.full_comps_calc(website, post_code, radius, minimum_beds, maximum_beds, "rent", percentile, auto_filter_on, save_flag)
 
    











