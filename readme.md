Programming Project: Bitsum

Please create a Django application that returns the number of bits set to 1 for the result of a multiplication of two numbers. More formally,

Write a function:

`def bitsum (A, B):`

That, given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation of the number A * B. For example, given A = 3 and B = 7, the function should return 3, because the binary representation of A * B = 3 * 7 = 10101 and it contains three bits set to 1. Assume that A and B are integers within the range of [0, ..., 100,000,000].

Please use Python and Django, and to installing the code it should just require running `pip install -r requirements.txt` from a virtual environment.

Use Postgres, MySql, MongoDB, Redis, Memcached, or similar database for persistence. Additionally, keep a tally of how many times the function is called, and each time it is called the counter is incremented. For example, before the function is called the counter should equal zero, then after the first time 1, and after that 2, and so on and so forth.

Querying `localhost:8000/bitsum?a=n&b=m` where n and m are any integers between 0 to 100,000,000, should return a JSON object that looks like the below:

{
  "time" : current_time,
  "bitsum": result,
  "A" : n,
  "B" : m,
  "used" : used_count
}

Have a frontend application with a list of the values requested so far, using the fields listed above, and a form to submit the number to be queried. You can use Backbone, jQuery, AngularJS, or any other frontend framework you like.

Submission: Commit your code using either git or mercurial using github, bitbucket, or a similar service.

