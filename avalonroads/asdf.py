
source_idx_file = "/home/lucas/codes/albion/avalonroads/source_idx.txt"
source_id_file = "/home/lucas/codes/albion/avalonroads/source_id.txt"
target_idx_file = "/home/lucas/codes/albion/avalonroads/target_idx.txt"
target_id_file = "/home/lucas/codes/albion/avalonroads/target_id.txt"

source_idx_stream = open(source_idx_file, "w")
source_id_stream = open(source_id_file, "w")
target_idx_stream = open(target_idx_file, "w")
target_id_stream = open(target_id_file, "w")

range_value = (1,9999)
for value in range(*range_value):
  source_idx_stream.write(f"=CORRESP(E{value};nodes!B2:B94;0)\n")
  source_id_stream.write(f"=ÍNDICE(nodes!A2:C94;CORRESP(E{value};nodes!B2:B94;0);1)\n")
  target_idx_stream.write(f"=CORRESP(E{value};nodes!B2:B94;0)\n")
  target_id_stream.write(f"=ÍNDICE(nodes!A2:C94;CORRESP(E{value};nodes!B2:B94;0);1)\n")
