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

| [`Day 7`](#pp_var_-4820698274011037134) has constant value "0" | Constant |
| [`Day 1`](#pp_var_-6493835625846555586) is highly overall correlated with `Day 2` and 2 other fields | High correlation |
| [`Day 2`](#pp_var_4429980805454742097) is highly overall correlated with `Day 1` and 2 other fields | High correlation |
| [`Day 3`](#pp_var_-4373165461308582805) is highly overall correlated with `Day 1` and 3 other fields | High correlation |
| [`Day 4`](#pp_var_-6726949964053177987) is highly overall correlated with `Day 6` and 1 other fields | High correlation |
| [`Day 5`](#pp_var_5301954561338592841) is highly overall correlated with `Day 6` and 1 other fields | High correlation |
| [`Day 6`](#pp_var_-1390173158940307628) is highly overall correlated with `Day 3` and 3 other fields | High correlation |
| [`Total`](#pp_var_-9009701641451579175) is highly overall correlated with `Day 1` and 5 other fields | High correlation |
| [`Total`](#pp_var_-9009701641451579175) is uniformly distributed | Uniform |
| [`Map`](#pp_var_5361061377961375898) has unique values | Unique |
| [`Total`](#pp_var_-9009701641451579175) has unique values | Unique |

Reproduction



| Analysis started | 2024\-09\-14 03:00:38\.814037 |
| --- | --- |
| Analysis finished | 2024\-09\-14 03:00:39\.419701 |
| Duration | 0\.61 seconds |
| Software version | [ydata\-profiling vv4\.10\.0](https://github.com/ydataai/ydata-profiling) |
| Download configuration | [config.json](data:text/plain;charset=utf-8,%7B%22title%22%3A%20%22Descriptive%20Statistics%20Report%22%2C%20%22dataset%22%3A%20%7B%22description%22%3A%20%22%22%2C%20%22creator%22%3A%20%22%22%2C%20%22author%22%3A%20%22%22%2C%20%22copyright_holder%22%3A%20%22%22%2C%20%22copyright_year%22%3A%20%22%22%2C%20%22url%22%3A%20%22%22%7D%2C%20%22variables%22%3A%20%7B%22descriptions%22%3A%20%7B%7D%7D%2C%20%22infer_dtypes%22%3A%20true%2C%20%22show_variable_description%22%3A%20true%2C%20%22pool_size%22%3A%200%2C%20%22progress_bar%22%3A%20true%2C%20%22vars%22%3A%20%7B%22num%22%3A%20%7B%22quantiles%22%3A%20%5B0.05%2C%200.25%2C%200.5%2C%200.75%2C%200.95%5D%2C%20%22skewness_threshold%22%3A%2020%2C%20%22low_categorical_threshold%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%7D%2C%20%22text%22%3A%20%7B%22length%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22redact%22%3A%20false%7D%2C%20%22cat%22%3A%20%7B%22length%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22cardinality_threshold%22%3A%2050%2C%20%22percentage_cat_threshold%22%3A%200.5%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22n_obs%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%2C%20%22coerce_str_to_date%22%3A%20false%2C%20%22redact%22%3A%20false%2C%20%22histogram_largest%22%3A%2050%2C%20%22stop_words%22%3A%20%5B%5D%7D%2C%20%22image%22%3A%20%7B%22active%22%3A%20true%2C%20%22exif%22%3A%20true%2C%20%22hash%22%3A%20true%7D%2C%20%22bool%22%3A%20%7B%22n_obs%22%3A%203%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22mappings%22%3A%20%7B%22t%22%3A%20true%2C%20%22f%22%3A%20false%2C%20%22yes%22%3A%20true%2C%20%22no%22%3A%20false%2C%20%22y%22%3A%20true%2C%20%22n%22%3A%20false%2C%20%22true%22%3A%20true%2C%20%22false%22%3A%20false%7D%7D%2C%20%22path%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22file%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22url%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22timeseries%22%3A%20%7B%22active%22%3A%20false%2C%20%22sortby%22%3A%20null%2C%20%22autocorrelation%22%3A%200.7%2C%20%22lags%22%3A%20%5B1%2C%207%2C%2012%2C%2024%2C%2030%5D%2C%20%22significance%22%3A%200.05%2C%20%22pacf_acf_lag%22%3A%20100%7D%7D%2C%20%22sort%22%3A%20null%2C%20%22missing_diagrams%22%3A%20%7B%22bar%22%3A%20true%2C%20%22matrix%22%3A%20true%2C%20%22heatmap%22%3A%20true%7D%2C%20%22correlation_table%22%3A%20true%2C%20%22correlations%22%3A%20%7B%22auto%22%3A%20%7B%22key%22%3A%20%22auto%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22spearman%22%3A%20%7B%22key%22%3A%20%22spearman%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22pearson%22%3A%20%7B%22key%22%3A%20%22pearson%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22phi_k%22%3A%20%7B%22key%22%3A%20%22phi_k%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22cramers%22%3A%20%7B%22key%22%3A%20%22cramers%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22kendall%22%3A%20%7B%22key%22%3A%20%22kendall%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%7D%2C%20%22interactions%22%3A%20%7B%22continuous%22%3A%20true%2C%20%22targets%22%3A%20%5B%5D%7D%2C%20%22categorical_maximum_correlation_distinct%22%3A%20100%2C%20%22memory_deep%22%3A%20true%2C%20%22plot%22%3A%20%7B%22missing%22%3A%20%7B%22force_labels%22%3A%20true%2C%20%22cmap%22%3A%20%22RdBu%22%7D%2C%20%22image_format%22%3A%20%22svg%22%2C%20%22correlation%22%3A%20%7B%22cmap%22%3A%20%22RdBu%22%2C%20%22bad%22%3A%20%22%23000000%22%7D%2C%20%22dpi%22%3A%20800%2C%20%22histogram%22%3A%20%7B%22bins%22%3A%2050%2C%20%22max_bins%22%3A%20250%2C%20%22x_axis_labels%22%3A%20true%2C%20%22density%22%3A%20false%7D%2C%20%22scatter_threshold%22%3A%201000%2C%20%22cat_freq%22%3A%20%7B%22show%22%3A%20true%2C%20%22type%22%3A%20%22bar%22%2C%20%22max_unique%22%3A%2010%2C%20%22colors%22%3A%20null%7D%2C%20%22font_path%22%3A%20null%7D%2C%20%22duplicates%22%3A%20%7B%22head%22%3A%2010%2C%20%22key%22%3A%20%22%23%20duplicates%22%7D%2C%20%22samples%22%3A%20%7B%22head%22%3A%2010%2C%20%22tail%22%3A%2010%2C%20%22random%22%3A%200%7D%2C%20%22reject_variables%22%3A%20true%2C%20%22n_obs_unique%22%3A%2010%2C%20%22n_freq_table_max%22%3A%2010%2C%20%22n_extreme_obs%22%3A%2010%2C%20%22report%22%3A%20%7B%22precision%22%3A%208%7D%2C%20%22html%22%3A%20%7B%22style%22%3A%20%7B%22primary_colors%22%3A%20%5B%22%23377eb8%22%2C%20%22%23e41a1c%22%2C%20%22%234daf4a%22%5D%2C%20%22logo%22%3A%20%22%22%2C%20%22theme%22%3A%20null%7D%2C%20%22navbar_show%22%3A%20true%2C%20%22minify_html%22%3A%20true%2C%20%22use_local_assets%22%3A%20true%2C%20%22inline%22%3A%20true%2C%20%22assets_prefix%22%3A%20null%2C%20%22assets_path%22%3A%20null%2C%20%22full_width%22%3A%20false%7D%2C%20%22notebook%22%3A%20%7B%22iframe%22%3A%20%7B%22height%22%3A%20%22800px%22%2C%20%22width%22%3A%20%22100%25%22%2C%20%22attribute%22%3A%20%22srcdoc%22%7D%7D%7D) |

Variables
=========

Select ColumnsMapTotalDay 1Day 2Day 3Day 4Day 5Day 6Day 7[Map](#pp_var_5361061377961375898)  
Text

`UNIQUE`  



| Distinct | 5 |
| --- | --- |
| Distinct (%) | 100\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 439\.0 B |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:39\.510835image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Overview](#5361061377961375898bottom-5361061377961375898overview)
* [Words](#5361061377961375898bottom-5361061377961375898word)
* [Characters](#5361061377961375898bottom-5361061377961375898characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:39\.831786image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [Characters](#5361061377961375898unicode-5361061377961375898characters)
* [Categories](#5361061377961375898unicode-5361061377961375898categories)
* [Scripts](#5361061377961375898unicode-5361061377961375898scripts)
* [Blocks](#5361061377961375898unicode-5361061377961375898blocks)

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

[Total](#pp_var_-9009701641451579175)  
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

 More details * [Overview](#-9009701641451579175bottom--9009701641451579175overview)
* [Categories](#-9009701641451579175bottom--9009701641451579175string)
* [Words](#-9009701641451579175bottom--9009701641451579175word)
* [Characters](#-9009701641451579175bottom--9009701641451579175characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:39\.995273image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:40\.136510image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 1 | 20\.0% |
| 9 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |
| 8 | 1 | 20\.0% |
| 12 | 1 | 20\.0% |

* [Characters](#-9009701641451579175unicode--9009701641451579175characters)
* [Categories](#-9009701641451579175unicode--9009701641451579175categories)
* [Scripts](#-9009701641451579175unicode--9009701641451579175scripts)
* [Blocks](#-9009701641451579175unicode--9009701641451579175blocks)

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

[Day 1](#pp_var_-6493835625846555586)  
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

 More details * [Overview](#-6493835625846555586bottom--6493835625846555586overview)
* [Categories](#-6493835625846555586bottom--6493835625846555586string)
* [Words](#-6493835625846555586bottom--6493835625846555586word)
* [Characters](#-6493835625846555586bottom--6493835625846555586characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:40\.276647image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:40\.397035image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

* [Characters](#-6493835625846555586unicode--6493835625846555586characters)
* [Categories](#-6493835625846555586unicode--6493835625846555586categories)
* [Scripts](#-6493835625846555586unicode--6493835625846555586scripts)
* [Blocks](#-6493835625846555586unicode--6493835625846555586blocks)

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

[Day 2](#pp_var_4429980805454742097)  
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

 More details * [Overview](#4429980805454742097bottom-4429980805454742097overview)
* [Categories](#4429980805454742097bottom-4429980805454742097string)
* [Words](#4429980805454742097bottom-4429980805454742097word)
* [Characters](#4429980805454742097bottom-4429980805454742097characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:40\.530880image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:40\.651570image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

* [Characters](#4429980805454742097unicode-4429980805454742097characters)
* [Categories](#4429980805454742097unicode-4429980805454742097categories)
* [Scripts](#4429980805454742097unicode-4429980805454742097scripts)
* [Blocks](#4429980805454742097unicode-4429980805454742097blocks)

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

[Day 3](#pp_var_-4373165461308582805)  
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

 More details * [Overview](#-4373165461308582805bottom--4373165461308582805overview)
* [Categories](#-4373165461308582805bottom--4373165461308582805string)
* [Words](#-4373165461308582805bottom--4373165461308582805word)
* [Characters](#-4373165461308582805bottom--4373165461308582805characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:40\.785799image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:40\.901984image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

* [Characters](#-4373165461308582805unicode--4373165461308582805characters)
* [Categories](#-4373165461308582805unicode--4373165461308582805categories)
* [Scripts](#-4373165461308582805unicode--4373165461308582805scripts)
* [Blocks](#-4373165461308582805unicode--4373165461308582805blocks)

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

[Day 4](#pp_var_-6726949964053177987)  
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

 More details * [Overview](#-6726949964053177987bottom--6726949964053177987overview)
* [Categories](#-6726949964053177987bottom--6726949964053177987string)
* [Words](#-6726949964053177987bottom--6726949964053177987word)
* [Characters](#-6726949964053177987bottom--6726949964053177987characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.031100image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.147774image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

* [Characters](#-6726949964053177987unicode--6726949964053177987characters)
* [Categories](#-6726949964053177987unicode--6726949964053177987categories)
* [Scripts](#-6726949964053177987unicode--6726949964053177987scripts)
* [Blocks](#-6726949964053177987unicode--6726949964053177987blocks)

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

[Day 5](#pp_var_5301954561338592841)  
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

 More details * [Overview](#5301954561338592841bottom-5301954561338592841overview)
* [Categories](#5301954561338592841bottom-5301954561338592841string)
* [Words](#5301954561338592841bottom-5301954561338592841word)
* [Characters](#5301954561338592841bottom-5301954561338592841characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.277624image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.393795image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

* [Characters](#5301954561338592841unicode-5301954561338592841characters)
* [Categories](#5301954561338592841unicode-5301954561338592841categories)
* [Scripts](#5301954561338592841unicode-5301954561338592841scripts)
* [Blocks](#5301954561338592841unicode-5301954561338592841blocks)

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

[Day 6](#pp_var_-1390173158940307628)  
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

 More details * [Overview](#-1390173158940307628bottom--1390173158940307628overview)
* [Categories](#-1390173158940307628bottom--1390173158940307628string)
* [Words](#-1390173158940307628bottom--1390173158940307628word)
* [Characters](#-1390173158940307628bottom--1390173158940307628characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.522435image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.638203image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

* [Characters](#-1390173158940307628unicode--1390173158940307628characters)
* [Categories](#-1390173158940307628unicode--1390173158940307628categories)
* [Scripts](#-1390173158940307628unicode--1390173158940307628scripts)
* [Blocks](#-1390173158940307628unicode--1390173158940307628blocks)

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

[Day 7](#pp_var_-4820698274011037134)  
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

 More details * [Overview](#-4820698274011037134bottom--4820698274011037134overview)
* [Categories](#-4820698274011037134bottom--4820698274011037134string)
* [Words](#-4820698274011037134bottom--4820698274011037134word)
* [Characters](#-4820698274011037134bottom--4820698274011037134characters)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.765046image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.873036image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

* [Characters](#-4820698274011037134unicode--4820698274011037134characters)
* [Categories](#-4820698274011037134unicode--4820698274011037134categories)
* [Scripts](#-4820698274011037134unicode--4820698274011037134scripts)
* [Blocks](#-4820698274011037134unicode--4820698274011037134blocks)

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:41\.949176image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

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

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:39\.109797image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ A simple visualization of nullity by column. xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-14T03:00:39\.353808image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Nullity matrix is a data\-dense display which lets you quickly visually pick out patterns in data completion. Sample
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

