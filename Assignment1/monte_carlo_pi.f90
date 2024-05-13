module point_module
    implicit none

    type :: Point
        real(kind=8) :: x
        real(kind=8) :: y
    end type Point

contains

    !generates a random value in the range (-0.5, 0.5).
    function random_val() result(retval)
        real(kind=8) :: retval


        call random_number(retval)
        retval = retval - 0.5  ! Shift to range (-0.5, 0.5)

    end function random_val

    !generates a random point 
    function random_point() result(retval)

        type(Point) :: retval

        retval%x = random_val()
        retval%y = random_val()

    end function random_point

    ! Monte Carlo method to estimate pi
    function monte_carlo_pi(num_points) result(pi)
        implicit none
        integer, intent(in) :: num_points
        real(kind=8) :: pi
        integer :: in_circle
        integer :: i
        type(Point) :: my_point
        in_circle = 0
        do i = 1, num_points
            my_point = random_point()
            if (my_point%x**2 + my_point%y**2 <= 0.25) then
                in_circle = in_circle + 1
            end if
        end do
        
        pi = 4.0 * in_circle / num_points

    end function monte_carlo_pi

end module point_module

! program mc
!     use point_module
!     implicit none

!     print *, monte_carlo_pi(1000)

! end program mc
