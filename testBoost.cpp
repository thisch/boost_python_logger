#include <iostream>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>

#include "PyLogger.hpp"

using namespace std;
using namespace boost::python;
using namespace log4espp;

std::shared_ptr<Logger> instance_a;
std::shared_ptr<Logger> instance_b;

void say_hello(const char* name) {
    instance_a->info(LOG4ESPP_LOCATION, name);
}

void other_func(void) {
    instance_b->info(LOG4ESPP_LOCATION, "from mshr");
    instance_b->debug(LOG4ESPP_LOCATION, "from mshr (dbg)");
    instance_b->error(LOG4ESPP_LOCATION, "from mshr (err)");
}

BOOST_PYTHON_MODULE(hello)
{
    cout << "BOOST MODULE BEGIN" << endl;
    def("say_hello", say_hello);
    def("other", other_func);

    PyLogger::registerPython();
    instance_a.reset(&Logger::getInstance("dolfin"));
    instance_b.reset(&Logger::getInstance("mshr"));
    cout << "BOOST MODULE END" << endl;
}
