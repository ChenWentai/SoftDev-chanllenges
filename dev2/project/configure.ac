
AC_INIT([project],[0.01],[cwentai01@gmail.com])

AM_INIT_AUTOMAKE([1.9 foreign])


AC_CONFIG_HEADERS([config.h])

AC_PROG_CC
AC_PROG_RANLIB
AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <mistery.h>]],\
                [[ mistery_value(1);]])],[AC_DEFINE([MISTERY_VALUE_ONEPARAM], [],[one parameter added])],[])
AC_SEARCH_LIBS([mistery_value],[magic vadoo mistery],[],[])
AC_CONFIG_FILES([Makefile  src/Makefile src/lib_foo/Makefile src/main/Makefile])
AC_OUTPUT


