Copr repository for git builds of freerdp, commits are fetched every hour.

The packages in this repo should work on Fedora 40+.



## Installation 

Activate the repo with `sudo dnf copr enable jackgreiner/freerdp-git` and then run `sudo dnf update --refresh`.

To revert this, remove the copr repository with `sudo dnf copr remove jackgreiner/freerdp-git` and then run `sudo dnf distro-sync` to download your distro's version of the freerdp package.


## Issues

Feel free to open issues when there are build issues I haven't fixed for a few days: https://github.com/ProjectSynchro/copr-freerdp-git/issues

If you'd like me to attempt to package this for other RPM based distros like SUSE, open an issue and I'll see what I can do :)

## Building Locally Using fedpkg

To build this package locally using `fedpkg`, follow these steps:

1. **Clone the Repository**:
    ```sh
    fedpkg clone -a https://github.com/ProjectSynchro/copr-freerdp-git.git
    cd copr-freerdp-git
    ```

2. **Install Dependencies**:
    ```sh
    sudo dnf install fedpkg
    sudo dnf builddep freerdp.spec
    ```

3. **Build the Package**:
    ```sh
    spectool -g freerdp.spec
    fedpkg local
    ```

This will create the RPM packages under a folder named by whatever arch you are building for in the current directory.

For more information on using `fedpkg`, refer to the [Fedora Packaging Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/).
