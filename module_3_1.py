call = 0

def count_calls():
    global call
    call +=1
    #print(call)

def string_info(string):
    count_calls()

    j= string.upper()
    k=string.lower()
    i=(len(string), j, k)
    print(i)
    #print(type(i))

def is_contains( string, list_to_search):
    count_calls()
    i=string.lower()
    m=(' '.join(map(str, list_to_search))).lower()
    #print(type(m))
    print(i in m)


string_info("capybara")
string_info("senior")

is_contains("NaME", ["name", "fnt", "mena"])
is_contains("baKE", ["bike", "bake", "kebab"])

print(call)