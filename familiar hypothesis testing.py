import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contincency

vein_pack_lifespans= familiar.lifespans(package='vein')
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test.pvalue)

if vein_pack_test.pvalue < 0.05:
  print("The Vein Pack is Proven to Make You Live Longer")
else:
    print("The Vein Pack is Probably Good For You Somehow!")

artery_pack_lifespans= familiar.lifespans(package='artery')
package_comparison_results= ttest_ind(vein_pack_test, artery_pack_lifespans)
print(package_comparison_results.pvalue)

iron_contingency_table= familiar.iron_counts_for_package()
_, iron_pvalue, _, _ = chi2_contincency(iron_contingency_table)
if  iron_pvalue < 0.05:
  print("The Artery Package Is Proven To Make You Healthier")
else:
  print(" While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
