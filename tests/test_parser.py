#!/usr/bin/env python
"""
Simple test script to verify that the refactored thaiaddress parser works.
"""

import thaiaddress

def test_basic_parsing():
    """Test basic parsing functionality"""
    result = thaiaddress.parse("นายปรายุ้ด จันทร์กะเพรา 099-999-9999 25/25 ถ.พุทธมณฑล สาย 4 ต. ศาลายา อ.พุทธมณฑล จ.นครปฐม 73170")
    print("Parsing result:")
    print(f"Name: {result['name']}")
    print(f"Address: {result['address']}")
    print(f"Location: {result['location']}")
    print(f"Subdistrict: {result['subdistrict']}")
    print(f"District: {result['district']}")
    print(f"Province: {result['province']}")
    print(f"Postal code: {result['postal_code']}")
    print(f"Phone number: {result['phone_number']}")
    print(f"Email: {result['email']}")
    
    # Basic validation
    assert result['name'] != ""
    assert result['phone_number'] != ""
    assert result['postal_code'] != ""
    
    return result

if __name__ == "__main__":
    print("Testing thaiaddress parser...")
    test_basic_parsing()
    print("Test completed successfully!")
