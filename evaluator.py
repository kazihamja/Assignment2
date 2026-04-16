def evaluate_file(input_path):
    results = []

    def tokenize(expr):
        tokens = []
        i = 0

        while i < len(expr):
            ch = expr[i]

            if ch.isdigit():
                num = ch
                i += 1
                while i < len(expr) and expr[i].isdigit():
                    num += expr[i]
                    i += 1
                tokens.append(("NUM", num))
                continue

            elif ch in "+-*/":
                tokens.append(("OP", ch))

            elif ch == "(":
                tokens.append(("LPAREN", ch))

            elif ch == ")":
                tokens.append(("RPAREN", ch))

            elif ch == " ":
                pass
            else:
                return "ERROR"

            i += 1

        tokens.append(("END", ""))
        return tokens


    def insert_implicit(tokens):
        new_tokens = []
        for i in range(len(tokens) - 1):
            t1 = tokens[i]
            t2 = tokens[i + 1]

            new_tokens.append(t1)

            if (t1[0] in ("NUM", "RPAREN") and t2[0] in ("NUM", "LPAREN")):
                new_tokens.append(("OP", "*"))

        new_tokens.append(tokens[-1])
        return new_tokens


    def parse(tokens):
        pos = 0

        def expr():
            nonlocal pos
            val, tree = term()

            while pos < len(tokens) and tokens[pos][1] in ("+", "-"):
                op = tokens[pos][1]
                pos += 1
                rval, rtree = term()

                if op == "+":
                    val += rval
                else:
                    val -= rval

                tree = f"({op} {tree} {rtree})"

            return val, tree


        def term():
            nonlocal pos
            val, tree = factor()

            while pos < len(tokens) and tokens[pos][1] in ("*", "/"):
                op = tokens[pos][1]
                pos += 1
                rval, rtree = factor()

                if op == "*":
                    val *= rval
                else:
                    if rval == 0:
                        raise Exception("div zero")
                    val /= rval

                tree = f"({op} {tree} {rtree})"

            return val, tree


        def factor():
            nonlocal pos
            tok_type, tok_val = tokens[pos]

            if tok_val == "-":
                pos += 1
                val, tree = factor()
                return -val, f"(neg {tree})"

            elif tok_type == "NUM":
                pos += 1
                return float(tok_val), tok_val

            elif tok_val == "(":
                pos += 1
                val, tree = expr()

                if tokens[pos][1] != ")":
                    raise Exception("missing )")

                pos += 1
                return val, tree

            else:
                raise Exception("invalid")

        val, tree = expr()
        return val, tree


    with open(input_path, "r") as f:
        lines = f.readlines()

    out = open("output.txt", "w")

    for line in lines:
        exp = line.strip()

        tokens = tokenize(exp)

        if tokens == "ERROR":
            tree = "ERROR"
            token_str = "ERROR"
            result = "ERROR"

        else:
            tokens = insert_implicit(tokens)

            try:
                value, tree = parse(tokens)

                # 🔥 CHANGED HERE (string → list)
                token_parts = []
                for t in tokens:
                    if t[0] != "END":
                        token_parts.append(f"[{t[0]}:{t[1]}]")
                token_parts.append("[END]")
                token_str = " ".join(token_parts)

                if int(value) == value:
                    result = int(value)
                else:
                    result = round(value, 4)

            except:
                tree = "ERROR"
                token_str = "ERROR"
                result = "ERROR"

        out.write(f"Input: {exp}\n")
        out.write(f"Tree: {tree}\n")
        out.write(f"Tokens: {token_str}\n")
        out.write(f"Result: {result}\n\n")

        results.append({
            "input": exp,
            "tree": tree,
            "tokens": token_str,
            "result": result
        })

    out.close()
    return results


# run
evaluate_file("sample_input.txt")
