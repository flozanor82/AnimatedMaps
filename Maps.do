
local RRs "C:\Users\floza\Desktop\Kosali Projects\SG_Add Files\Maps\"
use "C:\Users\floza\Desktop\Kosali Projects\SG_Add Files\Inputs\PDMP_quarterly_1998_2016.dta", clear

rename state statefips
rename statename state 

local Q1 "I"
local Q2 "II"
local Q3 "III" 
local Q4 "IV" 
local maps_ma ""
local maps_dl ""
local maps_da ""
local gp = 1
forvalues yr=2011(1)2016{
forvalues q=2(2)4{
	preserve
		keep if quarter==tq(`yr',`q')
		*Must Access
		local variable "pdmp_must"
		maptile `variable', geography(state) geoid(statefips) rangecolor(white blue) ndf(white) ///
			cutv(0.5)  ///
			twopt( ///
				legend(pos(6) ring(1) label(3 "Must Access States") label(2 "No Must Access States") size(small) rows(1)) ///
				t2title("`yr' - `Q`q''") name(ma_`yr'`q',replace)  )
		qui graph export "`RRs'MustAccess\MA_`gp'.png", as(png) replace
		local maps_ma "`maps_ma' ma_`yr'`q'"
		graph close
		*Delegate
		local variable "pdmp_daily"
		maptile `variable', geography(state) geoid(statefips) rangecolor(white emerald) ndf(white) ///
			cutv(0.5)  ///
			twopt( ///
				legend(pos(6) ring(1) label(3 "Daily Limit States") label(2 "No Daily Limit States") size(small) rows(1)) ///
				t2title("`yr' - `Q`q''") name(dl_`yr'`q',replace)	)
		qui graph export "`RRs'DailyLimit\DL_`gp'.png", as(png) replace
		local maps_dl "`maps_dl' dl_`yr'`q'"
		graph close
		*Delegate
		local variable "pdmp_delegate"
		maptile `variable', geography(state) geoid(statefips) rangecolor(white dkorange) ndf(white) ///
			cutv(0.5)  ///
			twopt( ///
				legend(pos(6) ring(1) label(3 "Delegate Allowance States") label(2 "No Delegate Allowance States") size(small) rows(1)) ///
				t2title("`yr' - `Q`q''") name(da_`yr'`q',replace)	)
		qui graph export "`RRs'DelegateAllow\DA_`gp'.png", as(png) replace
		local maps_da "`maps_da' da_`yr'`q'"
		graph close 
	restore
	local gp = `gp' + 1
}
}

grc1leg `maps_ma', graphregion(color(white)) legendfrom(ma_20164) pos(6) ring(1)  ///
				   title("PDMP - Introduciton of Must Access")
qui graph export "`RRs'MustAccess\Combined_MA.png", as(png) replace

grc1leg `maps_dl', graphregion(color(white)) legendfrom(dl_20164) pos(6) ring(1)  ///
				   title("PDMP - Introduciton of Daily Limits")
qui graph export "`RRs'DailyLimit\Combined_DL.png", as(png) replace			   

grc1leg `maps_da', graphregion(color(white)) legendfrom(da_20164) pos(6) ring(1)  ///
				   title("PDMP - Introduciton of Dellegate Allowance")
qui graph export "`RRs'DelegateAllow\Combined_DA.png", as(png) replace
