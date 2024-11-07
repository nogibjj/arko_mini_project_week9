
Descriptive Statistics ReportToggle navigation[Descriptive Statistics Report](#top)* [Overview](#overview)
* [Variables](#variables-dropdown)
* [Correlations](#correlations_tab)
* [Missing values](#missing)
* [Sample](#sample)
Overview
========

Brought to you by [YData](https://ydata.ai/?utm_source=opensource&utm_medium=ydataprofiling&utm_campaign=report)

* [Overview](#overview-dataset_overview)
* [Alerts 11](#overview-alerts)
* [Reproduction](#overview-reproduction)

Dataset statistics



| Number of variables | 9 |
| --- | --- |
| Number of observations | 5 |
| Missing cells | 0 |
| Missing cells (%) | 0\.0% |
| Duplicate rows | 0 |
| Duplicate rows (%) | 0\.0% |
| Total size in memory | 759\.0 B |
| Average record size in memory | 151\.8 B |

Variable types



| Text | 1 |
| --- | --- |
| Categorical | 8 |



Alerts

| [`Day 7`](#pp_var_514776310196006778) has constant value "0" | Constant |
| [`Day 1`](#pp_var_2457553518682759773) is highly overall correlated with `Day 2` and 2 other fields | High correlation |
| [`Day 2`](#pp_var_6332650989234284567) is highly overall correlated with `Day 1` and 2 other fields | High correlation |
| [`Day 3`](#pp_var_1811392739885579531) is highly overall correlated with `Day 1` and 3 other fields | High correlation |
| [`Day 4`](#pp_var_-7229350178357557580) is highly overall correlated with `Day 6` and 1 other fields | High correlation |
| [`Day 5`](#pp_var_7383151212883162597) is highly overall correlated with `Day 6` and 1 other fields | High correlation |
| [`Day 6`](#pp_var_3445321550912145115) is highly overall correlated with `Day 3` and 3 other fields | High correlation |
| [`Total`](#pp_var_-2373196864382598113) is highly overall correlated with `Day 1` and 5 other fields | High correlation |
| [`Total`](#pp_var_-2373196864382598113) is uniformly distributed | Uniform |
| [`Map`](#pp_var_-1694829432991126605) has unique values | Unique |
| [`Total`](#pp_var_-2373196864382598113) has unique values | Unique |

Reproduction



| Analysis started | 2024\-11\-07 20:55:54\.305958 |
| --- | --- |
| Analysis finished | 2024\-11\-07 20:55:55\.035467 |
| Duration | 0\.73 seconds |
| Software version | [ydata\-profiling vv4\.10\.0](https://github.com/ydataai/ydata-profiling) |
| Download configuration | [config.json](data:text/plain;charset=utf-8,%7B%22title%22%3A%20%22Descriptive%20Statistics%20Report%22%2C%20%22dataset%22%3A%20%7B%22description%22%3A%20%22%22%2C%20%22creator%22%3A%20%22%22%2C%20%22author%22%3A%20%22%22%2C%20%22copyright_holder%22%3A%20%22%22%2C%20%22copyright_year%22%3A%20%22%22%2C%20%22url%22%3A%20%22%22%7D%2C%20%22variables%22%3A%20%7B%22descriptions%22%3A%20%7B%7D%7D%2C%20%22infer_dtypes%22%3A%20true%2C%20%22show_variable_description%22%3A%20true%2C%20%22pool_size%22%3A%200%2C%20%22progress_bar%22%3A%20true%2C%20%22vars%22%3A%20%7B%22num%22%3A%20%7B%22quantiles%22%3A%20%5B0.05%2C%200.25%2C%200.5%2C%200.75%2C%200.95%5D%2C%20%22skewness_threshold%22%3A%2020%2C%20%22low_categorical_threshold%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%7D%2C%20%22text%22%3A%20%7B%22length%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22redact%22%3A%20false%7D%2C%20%22cat%22%3A%20%7B%22length%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22cardinality_threshold%22%3A%2050%2C%20%22percentage_cat_threshold%22%3A%200.5%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22n_obs%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%2C%20%22coerce_str_to_date%22%3A%20false%2C%20%22redact%22%3A%20false%2C%20%22histogram_largest%22%3A%2050%2C%20%22stop_words%22%3A%20%5B%5D%7D%2C%20%22image%22%3A%20%7B%22active%22%3A%20true%2C%20%22exif%22%3A%20true%2C%20%22hash%22%3A%20true%7D%2C%20%22bool%22%3A%20%7B%22n_obs%22%3A%203%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22mappings%22%3A%20%7B%22t%22%3A%20true%2C%20%22f%22%3A%20false%2C%20%22yes%22%3A%20true%2C%20%22no%22%3A%20false%2C%20%22y%22%3A%20true%2C%20%22n%22%3A%20false%2C%20%22true%22%3A%20true%2C%20%22false%22%3A%20false%7D%7D%2C%20%22path%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22file%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22url%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22timeseries%22%3A%20%7B%22active%22%3A%20false%2C%20%22sortby%22%3A%20null%2C%20%22autocorrelation%22%3A%200.7%2C%20%22lags%22%3A%20%5B1%2C%207%2C%2012%2C%2024%2C%2030%5D%2C%20%22significance%22%3A%200.05%2C%20%22pacf_acf_lag%22%3A%20100%7D%7D%2C%20%22sort%22%3A%20null%2C%20%22missing_diagrams%22%3A%20%7B%22bar%22%3A%20true%2C%20%22matrix%22%3A%20true%2C%20%22heatmap%22%3A%20true%7D%2C%20%22correlation_table%22%3A%20true%2C%20%22correlations%22%3A%20%7B%22auto%22%3A%20%7B%22key%22%3A%20%22auto%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22spearman%22%3A%20%7B%22key%22%3A%20%22spearman%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22pearson%22%3A%20%7B%22key%22%3A%20%22pearson%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22phi_k%22%3A%20%7B%22key%22%3A%20%22phi_k%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22cramers%22%3A%20%7B%22key%22%3A%20%22cramers%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22kendall%22%3A%20%7B%22key%22%3A%20%22kendall%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%7D%2C%20%22interactions%22%3A%20%7B%22continuous%22%3A%20true%2C%20%22targets%22%3A%20%5B%5D%7D%2C%20%22categorical_maximum_correlation_distinct%22%3A%20100%2C%20%22memory_deep%22%3A%20true%2C%20%22plot%22%3A%20%7B%22missing%22%3A%20%7B%22force_labels%22%3A%20true%2C%20%22cmap%22%3A%20%22RdBu%22%7D%2C%20%22image_format%22%3A%20%22svg%22%2C%20%22correlation%22%3A%20%7B%22cmap%22%3A%20%22RdBu%22%2C%20%22bad%22%3A%20%22%23000000%22%7D%2C%20%22dpi%22%3A%20800%2C%20%22histogram%22%3A%20%7B%22bins%22%3A%2050%2C%20%22max_bins%22%3A%20250%2C%20%22x_axis_labels%22%3A%20true%2C%20%22density%22%3A%20false%7D%2C%20%22scatter_threshold%22%3A%201000%2C%20%22cat_freq%22%3A%20%7B%22show%22%3A%20true%2C%20%22type%22%3A%20%22bar%22%2C%20%22max_unique%22%3A%2010%2C%20%22colors%22%3A%20null%7D%2C%20%22font_path%22%3A%20null%7D%2C%20%22duplicates%22%3A%20%7B%22head%22%3A%2010%2C%20%22key%22%3A%20%22%23%20duplicates%22%7D%2C%20%22samples%22%3A%20%7B%22head%22%3A%2010%2C%20%22tail%22%3A%2010%2C%20%22random%22%3A%200%7D%2C%20%22reject_variables%22%3A%20true%2C%20%22n_obs_unique%22%3A%2010%2C%20%22n_freq_table_max%22%3A%2010%2C%20%22n_extreme_obs%22%3A%2010%2C%20%22report%22%3A%20%7B%22precision%22%3A%208%7D%2C%20%22html%22%3A%20%7B%22style%22%3A%20%7B%22primary_colors%22%3A%20%5B%22%23377eb8%22%2C%20%22%23e41a1c%22%2C%20%22%234daf4a%22%5D%2C%20%22logo%22%3A%20%22%22%2C%20%22theme%22%3A%20null%7D%2C%20%22navbar_show%22%3A%20true%2C%20%22minify_html%22%3A%20true%2C%20%22use_local_assets%22%3A%20true%2C%20%22inline%22%3A%20true%2C%20%22assets_prefix%22%3A%20null%2C%20%22assets_path%22%3A%20null%2C%20%22full_width%22%3A%20false%7D%2C%20%22notebook%22%3A%20%7B%22iframe%22%3A%20%7B%22height%22%3A%20%22800px%22%2C%20%22width%22%3A%20%22100%25%22%2C%20%22attribute%22%3A%20%22srcdoc%22%7D%7D%7D) |

Variables
=========

Select ColumnsMapTotalDay 1Day 2Day 3Day 4Day 5Day 6Day 7[Map](#pp_var_-1694829432991126605)  
Text

`UNIQUE`  



| Distinct | 5 |
| --- | --- |
| Distinct (%) | 100\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 439\.0 B |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:55\.139441image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Overview](#-1694829432991126605bottom--1694829432991126605overview)
* [Words](#-1694829432991126605bottom--1694829432991126605word)
* [Characters](#-1694829432991126605bottom--1694829432991126605characters)

Length



| Max length | 6 |
| --- | --- |
| Median length | 5 |
| Mean length | 5\.2 |
| Min length | 4 |

Characters and Unicode



| Total characters | 26 |
| --- | --- |
| Distinct characters | 19 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 5 ? |
| --- | --- |
| Unique (%) | 100\.0% |

Sample



| 1st row | Ascent |
| --- | --- |
| 2nd row | Bind |
| 3rd row | Haven |
| 4th row | Icebox |
| 5th row | Split |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| ascent | 1 | 20\.0% |
| bind | 1 | 20\.0% |
| haven | 1 | 20\.0% |
| icebox | 1 | 20\.0% |
| split | 1 | 20\.0% |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:55\.568363image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [Characters](#-1694829432991126605unicode--1694829432991126605characters)
* [Categories](#-1694829432991126605unicode--1694829432991126605categories)
* [Scripts](#-1694829432991126605unicode--1694829432991126605scripts)
* [Blocks](#-1694829432991126605unicode--1694829432991126605blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

[Total](#pp_var_-2373196864382598113)  
Categorical

`HIGH CORRELATION`  `UNIFORM`  `UNIQUE`  



| Distinct | 5 |
| --- | --- |
| Distinct (%) | 100\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 419\.0 B |



| 2 | 1 |
| --- | --- |
| 9 | 1 |
| 3 | 1 |
| 8 | 1 |
| 12 | 1 |

 More details * [Overview](#-2373196864382598113bottom--2373196864382598113overview)
* [Categories](#-2373196864382598113bottom--2373196864382598113string)
* [Words](#-2373196864382598113bottom--2373196864382598113word)
* [Characters](#-2373196864382598113bottom--2373196864382598113characters)

Length



| Max length | 2 |
| --- | --- |
| Median length | 1 |
| Mean length | 1\.2 |
| Min length | 1 |

Characters and Unicode



| Total characters | 6 |
| --- | --- |
| Distinct characters | 5 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 5 ? |
| --- | --- |
| Unique (%) | 100\.0% |

Sample



| 1st row | 2 |
| --- | --- |
| 2nd row | 9 |
| 3rd row | 3 |
| 4th row | 8 |
| 5th row | 12 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 1 | 20\.0% |
| 9 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |
| 8 | 1 | 20\.0% |
| 12 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:55\.780268image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:55\.959036image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 1 | 20\.0% |
| 9 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |
| 8 | 1 | 20\.0% |
| 12 | 1 | 20\.0% |

* [Characters](#-2373196864382598113unicode--2373196864382598113characters)
* [Categories](#-2373196864382598113unicode--2373196864382598113categories)
* [Scripts](#-2373196864382598113unicode--2373196864382598113scripts)
* [Blocks](#-2373196864382598113unicode--2373196864382598113blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 6 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 6 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 6 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

[Day 1](#pp_var_2457553518682759773)  
Categorical

`HIGH CORRELATION`  



| Distinct | 4 |
| --- | --- |
| Distinct (%) | 80\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 2 |
| --- | --- |
| 2 | 1 |
| 1 | 1 |
| 3 | 1 |

 More details * [Overview](#2457553518682759773bottom-2457553518682759773overview)
* [Categories](#2457553518682759773bottom-2457553518682759773string)
* [Words](#2457553518682759773bottom-2457553518682759773word)
* [Characters](#2457553518682759773bottom-2457553518682759773characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 4 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 3 ? |
| --- | --- |
| Unique (%) | 60\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 2 |
| 3rd row | 0 |
| 4th row | 1 |
| 5th row | 3 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:56\.153087image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:56\.319531image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

* [Characters](#2457553518682759773unicode-2457553518682759773characters)
* [Categories](#2457553518682759773unicode-2457553518682759773categories)
* [Scripts](#2457553518682759773unicode-2457553518682759773scripts)
* [Blocks](#2457553518682759773unicode-2457553518682759773blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

[Day 2](#pp_var_6332650989234284567)  
Categorical

`HIGH CORRELATION`  



| Distinct | 4 |
| --- | --- |
| Distinct (%) | 80\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 2 |
| --- | --- |
| 3 | 1 |
| 1 | 1 |
| 2 | 1 |

 More details * [Overview](#6332650989234284567bottom-6332650989234284567overview)
* [Categories](#6332650989234284567bottom-6332650989234284567string)
* [Words](#6332650989234284567bottom-6332650989234284567word)
* [Characters](#6332650989234284567bottom-6332650989234284567characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 4 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 3 ? |
| --- | --- |
| Unique (%) | 60\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 3 |
| 3rd row | 0 |
| 4th row | 1 |
| 5th row | 2 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:56\.504048image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:56\.669760image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

* [Characters](#6332650989234284567unicode-6332650989234284567characters)
* [Categories](#6332650989234284567unicode-6332650989234284567categories)
* [Scripts](#6332650989234284567unicode-6332650989234284567scripts)
* [Blocks](#6332650989234284567unicode-6332650989234284567blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

[Day 3](#pp_var_1811392739885579531)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 1 | 3 |
| --- | --- |
| 0 | 1 |
| 3 | 1 |

 More details * [Overview](#1811392739885579531bottom-1811392739885579531overview)
* [Categories](#1811392739885579531bottom-1811392739885579531string)
* [Words](#1811392739885579531bottom-1811392739885579531word)
* [Characters](#1811392739885579531bottom-1811392739885579531characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 2 ? |
| --- | --- |
| Unique (%) | 40\.0% |

Sample



| 1st row | 1 |
| --- | --- |
| 2nd row | 1 |
| 3rd row | 1 |
| 4th row | 0 |
| 5th row | 3 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:56\.854832image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:57\.016180image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

* [Characters](#1811392739885579531unicode-1811392739885579531characters)
* [Categories](#1811392739885579531unicode-1811392739885579531categories)
* [Scripts](#1811392739885579531unicode-1811392739885579531scripts)
* [Blocks](#1811392739885579531unicode-1811392739885579531blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

[Day 4](#pp_var_-7229350178357557580)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 2 | 2 |
| --- | --- |
| 1 | 2 |
| 0 | 1 |

 More details * [Overview](#-7229350178357557580bottom--7229350178357557580overview)
* [Categories](#-7229350178357557580bottom--7229350178357557580string)
* [Words](#-7229350178357557580bottom--7229350178357557580word)
* [Characters](#-7229350178357557580bottom--7229350178357557580characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 1 ? |
| --- | --- |
| Unique (%) | 20\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 2 |
| 3rd row | 1 |
| 4th row | 2 |
| 5th row | 1 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:57\.196200image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:57\.356615image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

* [Characters](#-7229350178357557580unicode--7229350178357557580characters)
* [Categories](#-7229350178357557580unicode--7229350178357557580categories)
* [Scripts](#-7229350178357557580unicode--7229350178357557580scripts)
* [Blocks](#-7229350178357557580unicode--7229350178357557580blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

[Day 5](#pp_var_7383151212883162597)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 1 | 2 |
| --- | --- |
| 2 | 2 |
| 0 | 1 |

 More details * [Overview](#7383151212883162597bottom-7383151212883162597overview)
* [Categories](#7383151212883162597bottom-7383151212883162597string)
* [Words](#7383151212883162597bottom-7383151212883162597word)
* [Characters](#7383151212883162597bottom-7383151212883162597characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 1 ? |
| --- | --- |
| Unique (%) | 20\.0% |

Sample



| 1st row | 1 |
| --- | --- |
| 2nd row | 1 |
| 3rd row | 0 |
| 4th row | 2 |
| 5th row | 2 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:57\.535611image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:57\.696163image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

* [Characters](#7383151212883162597unicode-7383151212883162597characters)
* [Categories](#7383151212883162597unicode-7383151212883162597categories)
* [Scripts](#7383151212883162597unicode-7383151212883162597scripts)
* [Blocks](#7383151212883162597unicode-7383151212883162597blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

[Day 6](#pp_var_3445321550912145115)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 2 |
| --- | --- |
| 1 | 2 |
| 2 | 1 |

 More details * [Overview](#3445321550912145115bottom-3445321550912145115overview)
* [Categories](#3445321550912145115bottom-3445321550912145115string)
* [Words](#3445321550912145115bottom-3445321550912145115word)
* [Characters](#3445321550912145115bottom-3445321550912145115characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 1 ? |
| --- | --- |
| Unique (%) | 20\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 0 |
| 3rd row | 1 |
| 4th row | 2 |
| 5th row | 1 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:57\.873536image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:58\.037794image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

* [Characters](#3445321550912145115unicode-3445321550912145115characters)
* [Categories](#3445321550912145115unicode-3445321550912145115categories)
* [Scripts](#3445321550912145115unicode-3445321550912145115scripts)
* [Blocks](#3445321550912145115unicode-3445321550912145115blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

[Day 7](#pp_var_514776310196006778)  
Categorical

`CONSTANT`  



| Distinct | 1 |
| --- | --- |
| Distinct (%) | 20\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 5 |
| --- | --- |

 More details * [Overview](#514776310196006778bottom-514776310196006778overview)
* [Categories](#514776310196006778bottom-514776310196006778string)
* [Words](#514776310196006778bottom-514776310196006778word)
* [Characters](#514776310196006778bottom-514776310196006778characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 1 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 0 ? |
| --- | --- |
| Unique (%) | 0\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 0 |
| 3rd row | 0 |
| 4th row | 0 |
| 5th row | 0 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:58\.213447image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:58\.364574image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

* [Characters](#514776310196006778unicode-514776310196006778characters)
* [Categories](#514776310196006778unicode-514776310196006778categories)
* [Scripts](#514776310196006778unicode-514776310196006778scripts)
* [Blocks](#514776310196006778unicode-514776310196006778blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

Correlations
============

* [Auto](#correlations_tab-auto_diagram_table)

* [Heatmap](#auto_diagram_table-auto_diagram)
* [Table](#auto_diagram_table-auto_table)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:58\.471017image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

|  | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Day 1 | 1\.000 | 1\.000 | 0\.816 | 0\.000 | 0\.000 | 0\.000 | 1\.000 |
| Day 2 | 1\.000 | 1\.000 | 0\.816 | 0\.000 | 0\.000 | 0\.000 | 1\.000 |
| Day 3 | 0\.816 | 0\.816 | 1\.000 | 0\.000 | 0\.000 | 0\.577 | 1\.000 |
| Day 4 | 0\.000 | 0\.000 | 0\.000 | 1\.000 | 0\.000 | 0\.500 | 1\.000 |
| Day 5 | 0\.000 | 0\.000 | 0\.000 | 0\.000 | 1\.000 | 0\.500 | 1\.000 |
| Day 6 | 0\.000 | 0\.000 | 0\.577 | 0\.500 | 0\.500 | 1\.000 | 1\.000 |
| Total | 1\.000 | 1\.000 | 1\.000 | 1\.000 | 1\.000 | 1\.000 | 1\.000 |

Missing values
==============

* [Count](#missing-bar)
* [Matrix](#missing-matrix)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:54\.624661image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ A simple visualization of nullity by column. xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-11\-07T20:55:54\.943956image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Nullity matrix is a data\-dense display which lets you quickly visually pick out patterns in data completion. Sample
======

* [First rows](#sample-head)
* [Last rows](#sample-tail)



|  | Map | Total | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Ascent | 2 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | Bind | 9 | 2 | 3 | 1 | 2 | 1 | 0 | 0 |
| 2 | Haven | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 3 | Icebox | 8 | 1 | 1 | 0 | 2 | 2 | 2 | 0 |
| 4 | Split | 12 | 3 | 2 | 3 | 1 | 2 | 1 | 0 |



|  | Map | Total | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Ascent | 2 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | Bind | 9 | 2 | 3 | 1 | 2 | 1 | 0 | 0 |
| 2 | Haven | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 3 | Icebox | 8 | 1 | 1 | 0 | 2 | 2 | 2 | 0 |
| 4 | Split | 12 | 3 | 2 | 3 | 1 | 2 | 1 | 0 |

Report generated by [YData](https://ydata.ai/?utm_source=opensource&utm_medium=pandasprofiling&utm_campaign=report).

