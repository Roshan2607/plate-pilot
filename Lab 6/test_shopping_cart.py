"""
Unified Test Runner for Lab 6: Code and Branch Coverage
Software Engineering (UE24CS351A) - PES1UG24CS387
Executes full suite achieving >= 90% Code Coverage and >= 90% Branch Coverage.
"""

from BranchCoverageTest_23_shopping_cart import (
    test_item_total_valid_regular,
    test_item_total_bulk,
    test_item_total_unknown_category,
    test_item_total_negative_price,
    test_item_total_zero_quantity,
    test_cart_discount_all_tiers,
    test_shipping_lines,
    test_coupon_threshold_false_branch,
    test_express_prime_false_nested_branch,
    test_item_total_valid_price_and_quantity,
)
