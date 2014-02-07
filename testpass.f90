!module demonstrating how to pass functions to functions
module testpass
implicit none

contains

    function f(x)
        implicit none
        integer, intent(in) :: x
        integer :: f

        f=x*x
        return 
    end function

    function y(f) !with interface block

        interface 
            function f(x)
                integer :: x
                integer :: f
            end function
        end interface

        integer :: y

        y = f(3)
    end function

    function z(f) !works fine without

        integer :: f
        integer :: z

        z = f(5)
    end function

end module testpass

