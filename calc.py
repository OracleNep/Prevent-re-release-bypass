import argparse
import hashlib
import time
import random

def generate_sign(hex_value, token_value):
    # 生成随机字符串作为nonce_str
    nonce_str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
    # 获取当前时间戳（毫秒）
    timestamp = int(time.time() * 1000)
    
    # 构建待加密的数据
    data = f"token={token_value}&nonceStr={nonce_str}&timestamp={timestamp}"
    # 对数据进行MD5加密
    hash_data = hashlib.md5(data.encode()).hexdigest()
    # 将加密后的数据与自定义HEX值进行拼接并再次进行MD5加密得到签名值
    sign = hashlib.md5((hash_data + hex_value).encode()).hexdigest()
    
    return {
        "nonceStr": nonce_str,
        "timestamp": timestamp,
        "sign": sign
    }

def print_success_art():
    
    art = """
     _   _      _ _
    | | | | ___| | | ___
    | |_| |/ _ \ | |/ _ \\
    |  _  |  __/ | | (_) |
    |_| |_|\___|_|_|\___/
                       
    """
    print(art)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate sign based on custom hex and token values")
    
    # 添加命令行参数-H和-T，并指定帮助信息
    parser.add_argument("-H", "--hex", help="Custom HEX value", required=True)
    parser.add_argument("-T", "--token", help="Custom Token value", required=True)
    
    args = parser.parse_args()
    
     # 如果未提供必要参数，则打印帮助信息
if args.hex is None or args.token is None:
         parser.print_help()
else:
    result = generate_sign(args.hex, args.token)
        
    print("Noncestr:", result["nonceStr"])
    print("Timestamp:", result["timestamp"])
    print("Sign:", result["sign"])
        
    print_success_art()


