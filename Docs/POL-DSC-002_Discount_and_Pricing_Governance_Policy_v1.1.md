---
doc_id: POL-DSC-002
title: Discount & Pricing Governance Policy
company: Meridian Office Supply Co. (fictional)
version: 1.1
status: Active (hypothetical, generated for RAG testing)
effective_date: 2023-01-01
review_cycle: Semi-annual (Q1 and Q3)
owner: Commercial Finance
approver: Chief Financial Officer
applies_to: [all sales channels, all countries (France, Germany, Italy, USA), all categories (Furniture, Office Supplies, Technology)]
currency: USD
data_basis: "Orders 2018-2022 (11,807 order lines, $2.84M recorded sales, $303K recorded profit, 10.7% recorded margin)"
related_docs: [POL-RGN-001, POL-CUS-003]
tags: [discounting, pricing, margin, approval-matrix, binders, furniture, tables, clearance, loss-making-orders]
---

# Discount & Pricing Governance Policy (POL-DSC-002)

## 1. Purpose and scope

**DSC-1.1 Purpose.** This policy controls how discounts are granted so that discounting supports profitable growth. It sets approval authority, category caps, a hard block on very deep discounts, and monitoring rules.

**DSC-1.2 Why it exists (summary of evidence).** In 2018-2022, orders with no discount earned a **28.4% margin**, orders with a discount rate of 1-20% earned **10.4%**, and discount-rate bands above 20% were loss-making. Lines with a discount rate above 20% make up approximately **15.0% of order lines** and have a combined recorded profit of **-$178.1K**, equal to 58.8% of the company's five-year recorded profit ($303K).

**DSC-1.3 Scope.** Applies to every quote, order and contract that carries a discount, in every country and category.

## 2. Definitions

| Term | Definition |
|---|---|
| **Sales** | Recorded `Sales` amount in the Orders table. For this dataset, Sales is the recorded gross sales amount before applying the separate discount adjustment. |
| **Discount** | Absolute monetary discount per unit stored in the `Orders.Discount` field. It is **not** a percentage. |
| **Discount Rate** | Percentage reduction from the implied pre-discount unit price, derived as `Discount / (Unit_Price + Discount)`. All percentage discount figures in this policy refer to Discount Rate, not the raw `Orders.Discount` field. |
| **Margin** | `SUM(Profit) / SUM(Sales)` for the group being measured. |
| **Deep discount** | Discount Rate above 20%. This definition is used for the 15.0% deep-discount share reported in the evidence section. |
| **Clearance discount** | Discount Rate of 30% or more granted under the Clearance Exception in section 6. |
| **Blocked discount** | Discount Rate of 60% or more. Cannot be entered without a Clearance Exception. |
| **Loss-making order** | An order line with negative recorded Profit. |
| **Clearance Exception** | CFO-approved clearance discount used for end-of-life or excess stock (section 6). |

### 2.1 Discount data interpretation

The raw `Orders.Discount` value and the percentage Discount Rate must not be treated as interchangeable.

For an order line:

```text
Discount Rate = Discount / (Unit_Price + Discount)
```

The policy's percentage thresholds (10%, 20%, 30%, 60%, etc.) apply to **Discount Rate**.

## 3. Evidence: discount vs profitability

### 3.1 Margin by discount-rate band (all categories, 2018-2022)

| Discount-rate band | Order lines | Sales | Profit | Margin |
|---|---:|---:|---:|---:|
| 0% | 5,503 | $1,321.5K | $374.9K | **28.4%** |
| 1-20% | 4,536 | $1,026.2K | $106.3K | **10.4%** |
| 21-30% | 291 | $137.2K | -$14.2K | **-10.3%** |
| 31-50% | 392 | $279.2K | -$67.3K | **-24.1%** |
| 51-80% | 1,085 | $80.4K | -$96.6K | **-120.2%** |

**DSC-3.1.1 Break-even point.** Margin turns negative between 20% and 30% Discount Rate. At exactly 20% the margin is 9.9%; at 30% it is -10.3%.

**DSC-3.1.2 Common discount rates.** 10%: 18.1% margin (136 lines). 15%: 5.0% (62 lines). 20%: 9.9% (4,338 lines). 40%: -22.6%. 50%: -26.3%. 60%: -88.9%. 70%: -97.0% (508 lines). 80%: -184.2% (403 lines).

### 3.2 Margin by category and discount-rate band

| Category | 0% | 1-20% | 21-30% | 31-50% | 51-80% | Avg discount rate |
|---|---:|---:|---:|---:|---:|---:|
| Furniture | 22.0% | 5.4% | -11.2% | -36.6% | -105.8% | 18.0% |
| Office Supplies | 27.6% | 14.3% | (no lines) | (no lines) | -123.2% | 16.5% |
| Technology | 33.5% | 12.5% | 10.0% | -15.5% | -121.4% | 13.4% |

**DSC-3.2.1 Furniture.** Furniture has an overall margin of only 2.2%. Even a 1-20% discount rate cuts its margin to 5.4%, so Furniture has the least room to discount.

**DSC-3.2.2 Technology.** Technology is the only category that still earns a positive margin (10.0%) in the 21-30% discount-rate band, so it is the only category that may reach that band with approval.

### 3.3 Sub-categories with the highest discounting or losses

| Sub-category | Order lines | Avg discount rate | Margin |
|---|---:|---:|---:|
| Binders | 1,829 | 37.7% | 12.8% |
| Machines | 145 | 28.3% | -0.9% |
| Tables | 399 | 25.8% | **-7.7%** (-$21.3K profit) |
| Bookcases | 304 | 21.4% | -1.3% |
| Appliances | 590 | 20.4% | 11.7% |
| Supplies | 249 | 8.1% | -1.0% |

**DSC-3.3.1 Binders are the main source of deep discounting.** 755 of the 1,085 lines at a Discount Rate of 60% or more (69.6%) are Binders. Binder lines at 60%+ discount rate lost **$46.7K**, while the other 1,074 Binder lines earned **$75.5K**. Binders are profitable when not deeply discounted.

**DSC-3.3.2 Tables lose money even at moderate discount.** Tables have a -7.7% margin at an average discount rate of 25.8%. Bookcases and Machines are also loss-making overall.

**DSC-3.3.3 Supplies is not a discount problem.** Supplies loses money (-1.0%) at a low average discount rate of 8.1%, which points to a cost or list-price problem. The pricing review in section 7 applies.

### 3.4 Trend in deep discounting

| Year | Deep-discount share of lines | Net profit of deep-discount lines |
|---|---:|---:|
| 2018 | 13.4% | -$18.9K |
| 2019 | 14.9% | -$23.4K |
| 2020 | 14.8% | -$35.9K |
| 2021 | 15.3% | -$42.1K |
| 2022 | 15.4% | -$57.8K |

**DSC-3.4.1** Deep-discount losses tripled from -$18.9K (2018) to -$57.8K (2022) as sales grew 3.5 times. The problem is growing, not stabilising.

### 3.5 Losses overall

**DSC-3.5.1** 19.6% of all order lines are loss-making, totalling **-$204.1K**. The five worst single lines lost between $3,400 and $6,600 each.

**DSC-3.5.2 Discounting behaviour is uniform across countries.** Average discount rate: France 16.7%, Germany 16.4%, Italy 16.1%, USA 15.9%. Deep-discount share: France 15.4%, Germany 15.0%, Italy 14.2%, USA 14.7%. Deep discounting is a company-wide practice, not a single-country issue.

**DSC-3.5.3 Customers.** 693 of 800 customers (86.6%) received at least one deep-discount order, an average of 2.6 each. At customer level, average discount rate and margin are negatively correlated (-0.42).

## 4. Discount authority matrix

### 4.1 Approval levels

| Discount-rate requested | Approver | Conditions |
|---|---|---|
| 0-10% | Sales representative | Automatic. |
| 11-20% | Account manager | Order margin forecast must stay positive. |
| 21-30% | Regional director and Commercial Finance | **Technology only.** Finance margin check required. |
| 31-59% | Not permitted | Only via Clearance Exception (DSC-6.1). |
| 60% and above | **System-blocked** | Only via Clearance Exception (DSC-6.1). |

### 4.2 Category caps (standard operation)

| Category / sub-category | Maximum standard discount rate |
|---|---:|
| Furniture (all) | 15% |
| Tables and Bookcases | 10% |
| Office Supplies (all) | 20% |
| Binders | 20% |
| Machines | 15% |
| Technology (all other) | 30%, with approval per DSC-4.1 |

**DSC-4.3 Rationale for caps.** Furniture margin falls to 5.4% at 1-20% discount rate and negative above 20%; Tables, Bookcases and Machines lose money at their current average discount rates; Binders are profitable below deep discounts (DSC-3.3.1).

**DSC-4.4 Stacked discounts.** Multiple discounts on one line (promotion plus volume plus loyalty) are added together and tested against the caps. No combination may exceed the category cap.

## 5. Targets and monitoring

**DSC-5.1 Targets (rolling four quarters from effective date).**
1. Deep-discount share of order lines: from 15.0% to **under 5%**.
2. Loss-making order share: from 19.6% to **under 10%**.
3. Overall company margin: from 10.7% upward, tracked quarterly.

**DSC-5.2 Monitoring rules for the analytics pipeline.**
- Flag any order line with margin below -20% for Commercial Finance review within 5 business days.
- Report monthly: margin by discount-rate band, deep-discount share, and loss-making order share by category and country.
- Flag any customer whose average discount rate exceeds 20% (see POL-CUS-003, section 5).

**DSC-5.3 Metric definitions for analytics.** Discount-rate bands are 0; (0,20]; (20,30]; (30,50]; (50,100]. Margin is always `SUM(Profit)/SUM(Sales)` at the group level, never an average of line margins.

## 6. Exceptions

**DSC-6.1 Clearance Exception.** A clearance discount (30% or more Discount Rate) may be granted only when (a) the product is discontinued or overstocked, (b) Commercial Finance documents the expected loss, and (c) the CFO approves in writing. Total clearance volume is capped at **1% of quarterly sales**.

**DSC-6.2 Competitive match.** A discount rate up to the category cap plus 5 percentage points may be granted with a written competitor quote and Regional Director approval, provided the order margin stays positive.

**DSC-6.3 Strategic accounts.** Tier A accounts under POL-CUS-003 may receive up to the category cap but never above it. Account tier does not override the block in DSC-4.1.

**DSC-6.4 Large single orders.** Any order line above $10,000 in sales needs Commercial Finance review before confirmation, regardless of discount rate (in the data, the largest single lines reached $22,638 in sales).

**DSC-6.5 Grandfathering.** Contracts signed before 2023-01-01 keep their terms until renewal but are reported separately.

## 7. Country and sub-category pricing reviews

**DSC-7.1 Notable exceptions by country.** The sub-category margins below differ sharply from the company pattern and require a root-cause review (unit cost, list price, mix) before country-specific caps are set:

| Country | Sub-category | Margin | Comparison |
|---|---|---:|---|
| USA | Binders | **3.7%** | Italy 32.8%, Germany 21.8%, France 10.9% |
| France | Machines | **-9.8%** | Germany 10.5%, Italy 8.2%, USA 1.2% |
| Italy | Appliances | **-5.1%** | France 14.4%, USA 14.3%, Germany 7.5% |
| Italy | Supplies | **-17.6%** | France -0.7%, Germany -0.2%, USA -0.2% |

**DSC-7.2 Binders paradox.** Average Binder discount rate is nearly the same in every country (USA 36.6%, France 38.6%, Germany 37.9%, Italy 37.6%), yet USA margin is 3.7% and Italy 32.8%. The gap therefore comes from costs, list prices or product mix, not from discount depth. Until the review is complete, the global Binder cap (20%) applies everywhere.

**DSC-7.3 Persistent loss lines.** Tables, Bookcases, Supplies and Machines are reviewed twice a year for list-price or supplier-cost action. A sub-category that stays loss-making for four consecutive quarters is a candidate for delisting.

## 8. Governance

**DSC-8.1 Ownership.** Commercial Finance owns the matrix and reports to the CFO each quarter.

**DSC-8.2 Breaches.** Discounts that exceed the caps without approval are reported to the CFO. Repeat breaches by an individual are handled through the commission and performance process.

**DSC-8.3 Policy changes.** Caps are reviewed each Q1 and Q3 using the latest four quarters of margin by discount-rate band and category.

## 9. Data notes

**DSC-9.1** In the Orders data, `Sales` is approximately equal to `Unit_Price × Quantity` on typical lines, while the recorded `Discount` field is a separate absolute per-unit discount. Do not apply the Discount field a second time when recomputing Sales. About 1,641 lines deviate by more than 5% from the `Sales` versus `Unit_Price × Quantity` relationship and should be excluded or checked when reconciling.

**DSC-9.2** Profit is taken directly from the recorded `Profit` field. The policy does not infer an underlying cost formula from the available fields.

**DSC-9.3** All percentage discount figures in this document refer to the derived Discount Rate, not the raw `Orders.Discount` value.

## 10. Frequently asked questions

**Q: What is the maximum discount rate a sales rep can give without approval?** 10%.

**Q: Why are discount rates of 60% or more blocked?** Those lines lost $96.6K on $80.4K of sales (-120.2% margin), and 70% of them were Binders.

**Q: Can Furniture be discounted at a 25% discount rate?** No. The Furniture cap is 15% (10% for Tables and Bookcases); above 20% Furniture lost money in the data.

**Q: Which category can reach a 30% discount rate?** Only Technology, with Regional Director and Finance approval.

**Q: Is Binder discounting always bad?** No. Binder lines below 60% discount rate earned $75.5K. The loss comes from the 755 deep-discount lines.

**Q: Is any country worse at discounting?** No. All four countries average 16-17% discount rate and have 14-15% deep-discount shares.

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2023-01-01 | Initial issue. |
| 1.1 | 2026-09-30 | Clarified raw Discount vs derived Discount Rate; aligned deep-discount terminology; clarified Sales and Profit data semantics. |
