#!/usr/bin/env python3
"""
Test script to verify the updated endpoints.
"""

import logging
import fmpsdk

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_endpoint(name, func, api_key, *args, **kwargs):
    """
    Test an endpoint function and log the results.
    
    Args:
        name (str): Name of the endpoint function
        func (callable): The function to call
        api_key (str): API key to use
        *args: Additional positional arguments for the function
        **kwargs: Additional keyword arguments for the function
    
    Returns:
        bool: True if test passed, False otherwise
    """
    logging.info(f"Testing {name}...")
    try:
        result = func(api_key, *args, **kwargs)
        if result:
            if isinstance(result, list) and len(result) > 0:
                logging.info(f"Success! Received {len(result)} items.")
                logging.info(f"First item sample: {result[0]}")
                return True
            elif isinstance(result, dict):
                logging.info(f"Success! Received dictionary with {len(result)} keys.")
                logging.info(f"Keys: {list(result.keys())}")
                return True
            else:
                logging.warning(f"Endpoint returned unexpected result type: {type(result)}")
                return False
        else:
            logging.warning(f"Endpoint returned empty result: {result}")
            return False
    except Exception as e:
        logging.error(f"Error testing {name}: {e}")
        return False

def main():
    """Main function to test the updated endpoints."""
    # Use the API key from the .env file
    api_key = "5b9HBC68NX5mg3KWIRDnriOeu5jZQ2Jv"
    
    logging.info("Starting endpoint tests with FMP API key")
    
    # Test the endpoints we've updated to stable versions
    
    # Test market_indexes.py endpoints
    logging.info("\nTesting market_indexes.py endpoints:")
    test_endpoint("sp500_constituent", fmpsdk.sp500_constituent, api_key)
    test_endpoint("nasdaq_constituent", fmpsdk.nasdaq_constituent, api_key)
    test_endpoint("dowjones_constituent", fmpsdk.dowjones_constituent, api_key)
    test_endpoint("available_sectors", fmpsdk.available_sectors, api_key)
    
    # Test company_valuation.py endpoints
    logging.info("\nTesting company_valuation.py endpoints:")
    test_endpoint("company_profile", fmpsdk.company_profile, api_key, "AAPL")
    # test_endpoint("stock_peers", fmpsdk.stock_peers, api_key, "AAPL")  # Not directly exposed
    test_endpoint("available_industries", fmpsdk.available_industries, api_key)
    
    # Test institutional_fund.py endpoints
    logging.info("\nTesting institutional_fund.py endpoints:")
    test_endpoint("cik_list", fmpsdk.cik_list, api_key)
    test_endpoint("institutional_holders", fmpsdk.institutional_holders, api_key, "AAPL")
    
    # Test stock_market.py endpoints
    logging.info("\nTesting stock_market.py endpoints:")
    test_endpoint("actives", fmpsdk.actives, api_key)
    test_endpoint("gainers", fmpsdk.gainers, api_key)
    test_endpoint("losers", fmpsdk.losers, api_key)
    test_endpoint("market_hours", fmpsdk.market_hours, api_key)
    
    # Test bulk.py endpoints
    logging.info("\nTesting bulk.py endpoints:")
    test_endpoint("upgrades_downgrades_consensus_bulk", fmpsdk.upgrades_downgrades_consensus_bulk, api_key)
    
    logging.info("\nEndpoint tests completed")

if __name__ == "__main__":
    main()