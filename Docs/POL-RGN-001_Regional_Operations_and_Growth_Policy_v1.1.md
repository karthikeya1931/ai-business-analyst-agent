---
doc_id: POL-RGN-001
title: Regional Operations & Growth Policy
company: Meridian Office Supply Co. (fictional)
version: 1.1
status: Active (hypothetical, generated for RAG testing)
effective_date: 2023-01-01
review_cycle: Annual (Q1, after fiscal-year close)
owner: Regional Operations Committee (ROC)
approver: Chief Operating Officer
applies_to: [France, Germany, Italy, USA, US legacy sales regions (Central, East, South, West)]
currency: USD
data_basis: "Orders 2018-2022 (country level); USA_Sales 2011-2014 (US region and state level, last period with regional reporting)"
related_docs: [POL-DSC-002, POL-CUS-003]
tags: [regional-growth, operations, contraction, watchlist, growth-index, france, us-south, us-central, italy, germany]
---

# Regional Operations & Growth Policy (POL-RGN-001)

## 1. Purpose and scope

**RGN-1.1 Purpose.** This policy sets how Meridian Office Supply Co. measures regional growth and decides whether to expand, maintain, watch, or reduce operations in a region. It exists so that low-growth regions are treated consistently and on evidence, not case by case.

**RGN-1.2 Scope.** It applies to every operating unit. An *operating unit* is a **country** for the 2018-2022 order book (France, Germany, Italy, USA) and a **US sales region** (Central, East, South, West) for the legacy US regional history (2011-2014). US state/region reporting was discontinued after FY2014, so the 2014 data is the reference case used to test the rules below.

**RGN-1.3 What "reducing operations" means.** In this policy, reducing operations means one or more of the measures in section 5 (headcount freeze, fulfilment consolidation, narrowed field-sales coverage, paused acquisition spend). It never means abrupt withdrawal from serving existing customers.

## 2. Definitions

| Term | Definition |
|---|---|
| **Sales** | Recorded sales amount in USD for the operating unit in the applicable dataset and fiscal year. For the 2018-2022 order book, this refers to the recorded `Orders.Sales` field. For the 2011-2014 US regional analysis, it refers to the cleaned `USA_Sales.Sales` field. |
| **CAGR** | Compound annual growth rate over the full measurement window (2018-2022 for countries, 2011-2014 for US regions). |
| **Company CAGR** | CAGR of total recorded sales across all operating units in the same window. |
| **Growth Index (GI)** | Operating-unit CAGR divided by Company CAGR. GI = 1.00 means growing at the company rate. |
| **YoY** | Year-over-year change in recorded sales for the latest fiscal year. |
| **Stagnation Flag** | Operating-unit YoY below 5% while Company YoY is above 15%. |
| **Share** | Operating-unit recorded sales as a percentage of total company recorded sales in the latest year. |
| **Small-Base Rule** | A unit with under 10% of company sales is not ranked for expansion on GI alone (see RGN-6.3). |

## 3. Classification framework

**RGN-3.1 Tiers.** Each operating unit is assigned one tier at every annual review, based on its Growth Index:

| Tier | Growth Index (GI) | Meaning |
|---|---:|---|
| **Expand** | GI >= 1.15 | Priority for investment and capacity. |
| **Maintain** | 0.75 <= GI < 1.15 | Run at current resourcing. |
| **Watchlist** | 0.50 <= GI < 0.75 | Growth well below company pace. Remediation plan required. |
| **Contraction Review** | GI < 0.50 | Growth under half the company pace. Operations may be reduced under section 5. |

**RGN-3.2 Stagnation override.** A unit classified Maintain or Expand that trips the Stagnation Flag (RGN-2, definitions) is moved down one tier for the coming year.

**RGN-3.3 Margin check before contraction.** No unit may enter Contraction Review or have operations reduced if its operating margin is above the company margin **and** its YoY growth is positive. The margin check protects profitable slow growers.

**RGN-3.4 Company benchmark values.** For the 2018-2022 country window, Company CAGR is **36.3%** (recorded sales grew from $279K in 2018 to $965K in 2022) and company margin is **10.7%**. For the 2011-2014 US window, Company CAGR is **14.9%** (recorded sales grew from $484K to $734K).

## 4. Evidence: regional performance

### 4.1 Countries, 2018-2022

| Country | 2018 sales | 2022 sales | CAGR | Growth Index | 2022 YoY | 2022 share | Margin (5-yr) | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Germany | $67K | $317K | 47.2% | 1.30 | +47.4% | 32.9% | 12.1% | **Expand** |
| Italy | $13K | $75K | 56.3% | 1.55 | +42.8% | 7.8% | 10.9% | Expand (Small-Base Rule applies) |
| USA | $81K | $279K | 36.0% | 0.99 | +15.7% | 28.9% | 10.4% | **Maintain** (Deceleration Advisory) |
| France | $118K | $294K | 25.7% | 0.71 | +19.7% | 30.5% | 9.6% | **Watchlist** |

**RGN-4.1.1 Germany.** Germany grew fastest among the large markets and became the largest market in 2022 ($317K), passing France ($294K) and the USA ($279K). It also has the highest margin (12.1%) and the strongest Technology margin (19.7%).

**RGN-4.1.2 France.** France was the largest market in 2018 (42.2% of sales) and fell to 30.5% by 2022. It was the only country whose sales fell in 2019 (-18.7%, while every other country grew 42-70%). It has the lowest margin (9.6%) and its Machines sub-category loses money (-9.8% margin). France is classified **Watchlist** (GI 0.71).

**RGN-4.1.3 USA.** USA sits at GI 0.99 (Maintain) but its growth has decelerated: +61% (2019), +31% (2020), +40% (2021), +16% (2022). The 2022 YoY of 15.7% is 0.56 times the company YoY of 27.9%. This triggers a **Deceleration Advisory** (RGN-6.5), which is informational and does not change the tier.

**RGN-4.1.4 Italy.** Italy has the highest growth (GI 1.55) but only 59 customers and 7.8% of sales, so the Small-Base Rule applies. Italy also has loss-making Appliances (-5.1% margin) and Supplies (-17.6% margin).

### 4.2 US legacy regions, 2011-2014

| Region | 2011 sales | 2014 sales | CAGR | Growth Index | 2014 YoY | Retrospective tier |
|---|---:|---:|---:|---:|---:|---|
| West | $148K | $251K | 19.2% | 1.29 | +34.0% | **Expand** |
| East | $128K | $213K | 18.4% | 1.24 | +18.1% | **Expand** |
| Central | $104K | $147K | 12.3% | 0.83 | -0.2% | Maintain, moved to **Watchlist** by Stagnation Override |
| South | $104K | $123K | 5.8% | 0.39 | +31.5% | **Contraction Review** |

**RGN-4.2.1 South.** South had the lowest total sales ($392K over four years vs $726K for West) and the weakest growth (CAGR 5.8%, GI 0.39). It fell 31.3% in 2012, and did not exceed its 2011 level until 2014. Sales are concentrated: Florida, Virginia and North Carolina make up 55.1% of South sales across its 11 states. South is classified **Contraction Review**.

**RGN-4.2.2 Central.** Central grew 43.3% in 2013 but was flat in 2014 (-0.2%) while the company grew 20.6%. Texas alone is 34.0% of Central sales, and its Texas sales fell from $50.6K (2011) to $43.4K (2014). Central is classified **Watchlist** through the Stagnation Override (RGN-3.2).

**RGN-4.2.3 East and West.** West is 34.1% of 2014 sales and California alone is 63.1% of West sales. East depends on New York (45.8% of East sales). Both are Expand, with a concentration advisory (RGN-6.4).

## 5. Actions by tier

**RGN-5.1 Expand.** Priority capital and headcount. May add fulfilment capacity and sales coverage. Must keep discount discipline under POL-DSC-002.

**RGN-5.2 Maintain.** No new structural investment. Review at each annual cycle.

**RGN-5.3 Watchlist actions.**
1. A Remediation Plan is due within 60 days of classification.
2. Discretionary regional spend is capped at the prior-year level.
3. New headcount requires COO approval.
4. Discount exposure in the region is audited under POL-DSC-002.

**RGN-5.4 Contraction Review actions.** After the ROC confirms the classification, the following measures may be applied:
1. **Headcount freeze** and non-replacement of departures.
2. **Fulfilment consolidation** to hub states. For South, the hubs are Florida, Virginia and North Carolina (55.1% of regional sales).
3. **Narrowed field-sales coverage** to hub states; other states are served by inside sales and web channels.
4. **Paused new-customer acquisition spend** in non-hub states.
5. Existing customers keep service. Tier A and B accounts under POL-CUS-003 are exempt from service reductions.

**RGN-5.5 Duration and review.** Contraction measures are reviewed after two fiscal quarters. They are rolled back under the Recovery Rule (RGN-6.1) if the trigger no longer holds.

## 6. Exceptions and special rules

**RGN-6.1 Recovery Rule.** A unit leaves Contraction Review or Watchlist when it grows faster than the company for **two consecutive fiscal years**, or when its Growth Index recovers above the tier floor over a rolling three-year window. Illustration: South grew 31.1% in 2013 and 31.5% in 2014, both above the company rate for those years (29.3% and 20.6%); the second year meets the Recovery Rule and reverses measures 1 and 4 of RGN-5.4, while its tier stays Watchlist until the rolling GI is above 0.50.

**RGN-6.2 Rebound caution.** One strong year does not lift a tier. The 2014 South rebound came off a low 2012-2013 base and is not by itself proof of recovery.

**RGN-6.3 Small-Base Rule.** A unit with under 10% of company sales (currently Italy, 7.8%) is not given Expand-level investment on GI alone. Investment requires a business case that includes margin by sub-category.

**RGN-6.4 Concentration advisory.** If one state or city supplies more than 50% of a region's sales (California in West at 63.1%), the region carries a single-point-of-failure advisory and the ROC must review continuity risk annually.

**RGN-6.5 Deceleration Advisory.** If latest-year YoY is below 0.60 times Company YoY, the unit is flagged for management attention without a tier change. Currently applies to the USA (0.56).

**RGN-6.6 Local margin remediation.** Any city with at least $50,000 of lifetime recorded sales and a margin below 4% must have a Local Remediation Plan. Cities currently in scope: **Reims (France, 1.1%)**, **Lille (France, 2.6%)**, **Lander (USA, 3.1%)** and **Versailles (France, 3.3%)**. These four combine to $332K of recorded sales at 1-3% margin, so growth there is unprofitable.

**RGN-6.7 Shipping is not a differentiator.** Average order-to-ship time is 15.2 to 15.6 days in every country, with no material difference between markets. Shipping time is therefore not used as a reason to reduce operations in any region.

**RGN-6.8 Seasonality.** Sales peak in June-July and December ($260-271K monthly totals across 2018-2022) and trough in April and August-September ($210-216K). Temporary seasonal dips are not counted as regional stagnation; the growth tests use full fiscal years only.

## 7. Growth drivers (context for decisions)

**RGN-7.1 Growth comes from order frequency, not new customers.** Between 2018 and 2022 total order lines rose from 1,138 to 3,886 (3.4 times), while active customers rose only from 606 to 789. No new customers were first seen after 2020. Average recorded sales per order line stayed flat at about $228-248. Regional expansion decisions must therefore test whether existing customers can be served more often before funding new-market acquisition.

**RGN-7.2 Region mix of customers.** Customers: USA 254, France 246, Germany 241, Italy 59. Average lifetime recorded sales per customer: France $3,736, USA $3,560, Germany $3,440, Italy $3,256.

## 8. Governance

**RGN-8.1 Review process.** The ROC reviews all units each Q1 using the SQL/Python analytics pipeline, with recorded sales, margin and YoY computed from the relevant database. Results are recorded in the ROC minutes.

**RGN-8.2 Approval.** Watchlist and Contraction Review classifications need ROC majority approval. Contraction actions need COO sign-off.

**RGN-8.3 Appeals.** A regional lead may appeal a classification within 30 days with evidence that the data window is unrepresentative (for example, a one-off contract that inflated or depressed a year).

## 9. Data notes

**RGN-9.1 Sources.** Orders.csv (11,807 order lines, 2018-2022), Customers.csv (800 customers), Products.csv (1,850 products), USA_Sales.csv (9,992 rows, 2011-2014).

**RGN-9.2 Known data issues.** In USA_Sales, 471 Sales values use `;` as a thousands separator (for example `4;164`) and must be cleaned before numeric analysis. USA_Sales order IDs (format CA-2011-100006) do not link to Orders.csv, so US regional history is analysed separately. Order-level recorded Sales differ from Unit_Price x Quantity by more than 5% on 1,641 lines and by more than 20% on 583 lines, so margin analyses use the recorded Profit field.

**RGN-9.3 Dataset boundary.** Country-level analysis for 2018-2022 uses the Orders/Customers data. US regional and state-level analysis uses the separate USA_Sales dataset for 2011-2014. The two datasets must not be treated as one continuous regional time series.

## 10. Frequently asked questions

**Q: Why is France on the Watchlist?** Its Growth Index is 0.71 (CAGR 25.7% vs company 36.3%), it fell 18.7% in 2019, and it has the lowest margin at 9.6%.

**Q: Why was South placed under Contraction Review?** Its Growth Index of 0.39 is below the 0.50 floor, driven by a 31.3% drop in 2012 and the lowest total sales of the four US regions.

**Q: Why is Central on the Watchlist if its GI is 0.83?** Because 2014 sales were flat (-0.2%) while the company grew 20.6%, which trips the Stagnation Override.

**Q: Can a region be reduced if it is profitable?** Not if its margin is above the company margin and its growth is positive (RGN-3.3).

**Q: Does the USA face contraction?** No. Its GI is 0.99 (Maintain), with only a Deceleration Advisory.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2023-01-01 | Initial issue. |
| 1.1 | 2026-09-30 | Clarified recorded Sales terminology and dataset boundaries; distinguished current country data from historical US regional data; clarified order-line terminology. |
