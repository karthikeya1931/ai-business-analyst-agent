---
doc_id: POL-CUS-003
title: Customer Segmentation & Credit Policy
company: Meridian Office Supply Co. (fictional)
version: 1.0
status: Active (hypothetical, generated for RAG testing)
effective_date: 2023-01-01
review_cycle: Quarterly re-tiering, annual policy review
owner: Customer Finance and Sales Operations
approver: Chief Financial Officer
applies_to: [all 800 B2B customers in France, Germany, Italy, USA]
currency: USD
data_basis: "Orders 2018-2022 joined to Customers (800 customers). Reference date for recency: 2022-12-31."
related_docs: [POL-RGN-001, POL-DSC-002]
tags: [customer-tiers, segmentation, credit-limits, loss-making-customers, margin-recovery, customer-score, dormant-customers, strategic-accounts]
---

# Customer Segmentation & Credit Policy (POL-CUS-003)

## 1. Purpose and scope

**CUS-1.1 Purpose.** This policy groups customers into tiers, sets credit limits and payment terms by tier, and defines actions for loss-making, low-margin and dormant customers.

**CUS-1.2 Scope.** All 800 customers on record. The first tier assignment uses cumulative 2018-2022 sales; from 2023 tiers are recalculated every quarter on trailing 24-month sales.

**CUS-1.3 Assumption on credit data.** The source data contains sales, profit and a customer Score, but no payment or receivables history. Credit limits and terms in section 4 are therefore based on sales history; payment-behaviour triggers will be added once receivables data is available.

## 2. Definitions

| Term | Definition |
|---|---|
| Customer sales | Total Sales for a customer over the measurement window. |
| Customer margin | SUM(Profit) / SUM(Sales) for that customer. |
| Loss-making customer | A customer whose total Profit over the window is negative. |
| Margin Watch customer | A customer with sales above $5,000 and margin below 5%. |
| Dormant customer | No order in the last 180 days (measured to the review date). |
| Lapsed customer | No order in the last 365 days. |
| Customer Score | A 0-100 score held in the CRM. Advisory only (see CUS-3.3). |
| Average discount | Mean of Discount across the customer's order lines. |

## 3. Evidence: what the customer base looks like

### 3.1 Base and concentration

**CUS-3.1.1 Base size.** 800 customers: USA 254, France 246, Germany 241, Italy 59. Every customer has ordered; on average each has about 14.8 order lines.

**CUS-3.1.2 Concentration is moderate.** The top 10% of customers (80) generate 27.6% of sales and the top 20% (160) generate 43.1%. Sales are spread widely, so losing one customer has limited impact.

**CUS-3.1.3 No customers acquired after 2020.** 606 customers were first seen in 2018, 162 in 2019 and 32 in 2020; none after. Active customers grew from 606 (2018) to 789 (2022), while order lines rose from 1,138 to 3,886. Growth has come from existing customers ordering more often.

### 3.2 Tier profile (by cumulative sales rank, 2018-2022)

| Tier | Rank rule | Customers | Share of sales | Margin | Avg order lines | Avg discount |
|---|---|---|---|---|---|---|
| **A: Strategic** | Top 10% | 80 | 27.6% ($786K) | 11.4% | 17.4 | 16.5% |
| **B: Key** | Next 20% | 160 | 27.7% ($787K) | 10.6% | 16.6 | 15.3% |
| **C: Core** | Next 40% | 320 | 33.0% ($939K) | 10.1% | 14.8 | 16.4% |
| **D: Standard** | Bottom 30% | 240 | 11.7% ($332K) | 10.5% | 12.7 | 16.6% |

**CUS-3.2.1** Margin is similar across tiers (10.1% to 11.4%), so bigger customers are not meaningfully more profitable per dollar. Tier A has the highest margin and Tier C the lowest.

### 3.3 Customer Score is not predictive

**CUS-3.3.1** The Score has almost no relationship with behaviour. Correlation with customer sales is 0.03, with profit 0.08 and with order count 0.00.

| Score band | Customers | Avg lifetime sales | Total profit |
|---|---|---|---|
| 0-25 | 253 | $3,537 | $80.9K |
| 26-50 | 196 | $3,589 | $61.6K |
| 51-75 | 176 | $3,495 | $78.2K |
| 76-100 | 175 | $3,606 | $82.4K |

**CUS-3.3.2 Score by country (average).** Italy 52.6, Germany 47.6, France 46.8, USA 42.0.

**CUS-3.3.3 Consequence.** The Score must not be the sole basis for credit limits, terms or discount rights. It may be used as one advisory input alongside sales history.

### 3.4 Loss-making and low-margin customers

**CUS-3.4.1 Size of the problem.** 144 customers (18.0%) are loss-making, with combined sales of $551.5K and a combined net loss of **-$78.6K**. A further **36 customers** are Margin Watch (sales above $5,000, margin below 5%).

| Country | Loss-making customers | Share of country base | Net loss |
|---|---|---|---|
| France | 52 | 21.1% | -$38.3K |
| USA | 43 | 16.9% | -$23.6K |
| Germany | 41 | 17.0% | -$13.4K |
| Italy | 8 | 13.6% | -$3.3K |

**CUS-3.4.2 Discount is the driver.** Loss-making customers average a 20.3% discount, against 15.4% for profitable customers. Across all customers, average discount and margin have a correlation of -0.42.

**CUS-3.4.3 Big does not mean valuable.** Of the five largest customers by sales, three are loss-making: customer 457 (USA, $28.5K sales, -$1.2K profit), customer 82 (USA, $26.3K, -$1.1K) and customer 58 (France, $24.3K, -$1.9K). Customer 488 (Germany, $22.9K) earned only $0.3K. By contrast customer 690 (Germany, $23.3K) earned $9.5K. Size alone must not earn favourable terms.

### 3.5 Recency

**CUS-3.5.1** As of 2022-12-31, the median customer last ordered 52 days earlier and the 75th percentile is 104 days. **67 customers are Dormant** (over 180 days) and **11 are Lapsed** (over 365 days; longest gap 716 days).

## 4. Tiers, credit limits and terms

**CUS-4.1 Credit and terms by tier.**

| Tier | Credit limit (share of trailing 12-month sales) | Minimum limit | Payment terms | Review |
|---|---|---|---|---|
| A: Strategic | 25% | $2,500 | Net 45 | Quarterly |
| B: Key | 20% | $1,500 | Net 30 | Quarterly |
| C: Core | 15% | $1,000 | Net 30 | Semi-annual |
| D: Standard | 10% | $500 | Net 15 | Semi-annual |

**CUS-4.2 Score as a secondary input.** A customer with a Score below 25 may not be moved up a tier for terms purposes without Customer Finance sign-off, but Score never lowers terms by itself (CUS-3.3.3).

**CUS-4.3 Margin gate on terms.** No customer may hold Tier A or Tier B terms while classified loss-making for two consecutive quarters (see section 5).

**CUS-4.4 New customers.** New customers start at Tier D terms (Net 15, minimum limit) for their first two orders, then are tiered on actual sales.

## 5. Actions for loss-making, Margin Watch, dormant and lapsed customers

**CUS-5.1 Loss-making customers.**
1. Placed on a **Margin Recovery Plan** within 90 days.
2. Discount authority for that customer is limited to 10% (Account Manager cannot exceed it) until margin turns positive (see POL-DSC-002).
3. After two quarters of negative margin: reprice future orders or reduce eligible product mix (Tables, Bookcases, Machines).
4. After four quarters of negative margin: downgrade one tier for terms and credit.

**CUS-5.2 Margin Watch customers (sales above $5,000, margin below 5%).** Discount above 10% needs Regional Director approval. Reviewed quarterly.

**CUS-5.3 High-discount flag.** A customer with average discount above 20% over the last four quarters is flagged for account review. This matches the monitoring rule in POL-DSC-002 (DSC-5.2).

**CUS-5.4 Dormant customers (over 180 days).** Sales Operations runs a reactivation contact. Credit limit is frozen at the last approved value.

**CUS-5.5 Lapsed customers (over 365 days).** Credit limit is reduced to the Tier D minimum. On reactivation the customer restarts under CUS-4.4.

## 6. Exceptions

**CUS-6.1 Strategic-account exception.** A Tier A customer that is loss-making (for example customers 457, 82 and 58) is not dropped or downgraded immediately. It gets a Margin Recovery Plan with a 90-day target, and keeps Tier A terms while the plan is on track. The margin gate in CUS-4.3 is suspended for one review cycle only.

**CUS-6.2 Small-sample exception.** A customer with fewer than 5 order lines in the window is not classified loss-making or Margin Watch, because a single large discounted order can dominate its margin.

**CUS-6.3 Regional exemption.** Customers in a region under Contraction Review in POL-RGN-001 keep their tier terms. Tier A and B customers are exempt from service reductions.

**CUS-6.4 Ties with regional watchlist.** France has the highest share of loss-making customers (21.1%) and is on the regional Watchlist. A France-specific Margin Recovery drive is part of its remediation plan.

**CUS-6.5 Score override.** A Score of 76-100 does not entitle a customer to a discount above the caps in POL-DSC-002, and does not offset a negative margin.

## 7. Growth and retention

**CUS-7.1 Acquisition gap.** No new customers appeared after 2020. Sales Operations must present a customer-acquisition plan each year, focused first on markets not under Contraction Review.

**CUS-7.2 Retention focus.** Because growth comes from ordering frequency, the retention metric is order lines per active customer (2022: 3,886 order lines across 789 active customers, about 4.9 per customer per year).

**CUS-7.3 Reporting.** Quarterly dashboard: tier counts and sales share, loss-making and Margin Watch counts, dormant and lapsed counts, average discount by tier, and Score vs margin.

## 8. Governance

**CUS-8.1 Ownership.** Customer Finance owns tiering and limits; Sales Operations owns recovery plans and reactivation.

**CUS-8.2 Approvals.** Credit limit changes above $10,000 need CFO approval. Tier exceptions need Regional Director and Customer Finance approval.

**CUS-8.3 Data.** Tiering is computed from the order database (SQL for aggregates, Python for scoring and flags). Customer margin must use SUM(Profit)/SUM(Sales), not an average of line margins.

## 9. Frequently asked questions

**Q: How many customers are loss-making?** 144 of 800 (18.0%), with a combined net loss of $78.6K.

**Q: Which country has the most loss-making customers?** France, with 52 customers and -$38.3K.

**Q: Does a high Customer Score give better credit terms?** No. The Score has near-zero correlation with sales (0.03) and profit (0.08), so it is advisory only.

**Q: Are our biggest customers our most profitable?** Not necessarily. Three of the five largest customers by sales are loss-making.

**Q: What credit limit does a Tier B customer get?** 20% of trailing 12-month sales, minimum $1,500, on Net 30 terms.

**Q: What happens to a loss-making Tier A customer?** A 90-day Margin Recovery Plan, a 10% discount limit, and downgrade only if margin stays negative for four quarters.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2023-01-01 | Initial issue. |
